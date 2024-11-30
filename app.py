import os
import cv2
from flask import Flask, render_template, request, redirect, send_from_directory
from ultralytics import YOLO

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'mp4', 'png', 'jpg', 'jpeg'}

# Load the YOLOv8 helmet detection model directly
helmet_model = YOLO('C:\\Users\\BUJJI\\Downloads\\Bike Helmet Detection.v2i.yolov8\\runs\\detect\\helmet_detection3\\weights\\best.pt')
# Function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Route for the main page
@app.route('/')
def index():
    return render_template('index.html')

# Route for handling video upload
@app.route('/upload_video', methods=['POST'])
def upload_video():
    if 'video' not in request.files:
        return redirect(request.url)
    file = request.files['video']
    if file and allowed_file(file.filename):
        filename = file.filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        output_video_path = detect_from_video(filepath)
        return send_from_directory(app.config['UPLOAD_FOLDER'], os.path.basename(output_video_path), as_attachment=True)
    return redirect(request.url)

# Route for handling image upload
@app.route('/upload_image', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return redirect(request.url)
    file = request.files['image']
    if file and allowed_file(file.filename):
        filename = file.filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        output_image_path = detect_from_image(filepath)
        return send_from_directory(app.config['UPLOAD_FOLDER'], os.path.basename(output_image_path), as_attachment=True)
    return redirect(request.url)

# Route for real-time detection
@app.route('/realtime', methods=['POST'])
def realtime_detection():
    cap = cv2.VideoCapture(0)  # Use 0 for the default camera
    if not cap.isOpened():
        return "Camera not accessible", 400
    output_video_path = os.path.join(app.config['UPLOAD_FOLDER'], 'realtime_output.mp4')
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_video_path, fourcc, 20.0, (640, 480))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame = detect_on_frame(frame)
        out.write(frame)
    cap.release()
    out.release()
    return send_from_directory(app.config['UPLOAD_FOLDER'], 'realtime_output.mp4', as_attachment=True)

# Detection function for video files
def detect_from_video(video_path):
    cap = cv2.VideoCapture(video_path)
    output_path = os.path.join(app.config['UPLOAD_FOLDER'], 'output_video.mp4')
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame = detect_on_frame(frame)
        out.write(frame)
    cap.release()
    out.release()
    return output_path

# Detection function for image files
def detect_from_image(image_path):
    frame = cv2.imread(image_path)
    frame = detect_on_frame(frame)
    output_image_path = os.path.join(app.config['UPLOAD_FOLDER'], 'output_image.jpg')
    cv2.imwrite(output_image_path, frame)
    return output_image_path

# Function to perform detection on a frame
def detect_on_frame(frame):
    helmet_results = helmet_model.predict(source=frame, save=False, conf=0.5)
    for result in helmet_results[0].boxes:
        x1, y1, x2, y2 = map(int, result.xyxy[0])
        conf = result.conf[0]
        cls = int(result.cls[0])
        class_name = helmet_model.names[cls]

        # Set the label and color based on the detection
        if class_name.lower() == 'with helmet':
            color = (0, 255, 0)
            label = "Helmet Detected"
        elif class_name.lower() == 'without helmet':
            color = (0, 0, 255)
            label = "No Helmet"

        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
        cv2.putText(frame, f"{label} ({conf:.2f})", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)
   
    return frame

if __name__ == '__main__':
    app.run(debug=True)
