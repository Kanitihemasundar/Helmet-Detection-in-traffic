Helmet Detection System 🚴‍♂️🛵
This project is a helmet detection system that uses YOLOv8 and OpenCV to detect whether a person on a motorcycle is wearing a helmet or not. It processes video input, identifies motorcycles, and highlights detection results with labels for "with helmet" (green) and "without helmet" (red). The project includes a user-friendly Flask-based web interface for real-time video uploads and downloadable results.

🚀 Features
Video Upload: Upload videos directly through the web interface for processing.
Real-Time Detection: Detect people, motorcycles, and helmets in the uploaded video frames.
Labeling System:
Green label: Indicates helmets detected.
Red label: Indicates no helmet detected.
Download Output: Once processing is complete, download the labeled video file as output.
Frontend Interface:
Colorful and intuitive web design built with Flask.
Buttons for uploading videos, images, or real-time detection via webcam.
🖥️ Tech Stack
Backend
YOLOv8 for object detection
OpenCV for video processing
Flask for web application development
Frontend
HTML, CSS, Bootstrap for styling
JavaScript for interactivity
🛠️ Setup Instructions
Prerequisites
Ensure you have the following installed:

Python 3.8+
pip (Python package manager)
Installation
Clone this repository:

bash
Copy code
git clone https://github.com/your-username/helmet-detection-system.git  
cd helmet-detection-system  
Install the required Python libraries:

bash
Copy code
pip install -r requirements.txt  
Download the YOLOv8 model weights and place them in the models/ directory:

Example: models/yolov8-helmet-detection.pt
Verify that your dataset YAML file (data.yaml) and pre-trained model are correctly set up for YOLOv8.

▶️ How to Use
Start the Flask server:

bash
Copy code
python app.py  
Open your browser and navigate to:
http://127.0.0.1:5000

Upload your video using the Upload Video button.

Wait for the detection process to complete.

Download the processed video file with helmet detection results.

📂 Project Structure
plaintext
Copy code
helmet-detection-system/  
│  
├── app.py                 # Main Flask application  
├── models/                # YOLOv8 model weights  
├── static/                # Frontend assets (CSS, JS, images)  
├── templates/             # HTML templates for Flask  
├── uploads/               # Uploaded video files  
├── outputs/               # Processed video outputs  
├── data.yaml              # Dataset configuration for YOLOv8  
├── requirements.txt       # Python dependencies  
└── README.md              # Project documentation  
🎉 Output Example
After processing, the output is a video file that includes:

Detected objects (motorcycle and helmet) with bounding boxes and labels.
Green labels for riders with helmets and red labels for those without helmets.
You can download this processed video directly from the web interface.

👩‍💻 Contributions
contribute to this project by: K.Hemasundar(L), K.Latish, R.Sunil, R.Chinni Krishna

Reporting bugs.
Suggesting improvements or features.
Submitting pull requests.


🙌 Acknowledgments
YOLOv8 for advanced object detection.
Flask and OpenCV for simplifying backend integration.
