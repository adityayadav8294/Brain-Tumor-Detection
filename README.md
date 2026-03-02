# 🧠 Brain Tumor Detection and Classification

A deep learning-based web application for detecting and classifying brain tumors from MRI images using a Convolutional Neural Network (CNN).

---

## 📌 Project Overview

This system allows users to upload MRI brain scan images and receive:

- Tumor type prediction
- Confidence score
- Fast web-based inference
- Clean and responsive interface

Designed for academic research, medical AI demonstrations, and machine learning portfolio projects.

---

## 🎯 Classification Categories

The model classifies MRI images into:

- Glioma Tumor
- Meningioma Tumor
- Pituitary Tumor
- No Tumor

---

## 🛠 Tech Stack

### Backend
- Python 3.10
- Flask
- Gunicorn
- TensorFlow (Keras)
- NumPy
- h5py
- Pillow

### Frontend
- HTML5
- CSS3
- Bootstrap
- Jinja2 Templates

### Deployment
- Render (Cloud Hosting)
- Git & GitHub

---

## 🧠 Model Details

- Model Type: Convolutional Neural Network (CNN)
- Framework: TensorFlow / Keras
- Model Format: `.h5`
- Input Size: 128x128 pixels
- Image Normalization: Pixel scaling (0–1 range)
- Output Layer: Softmax activation
- Prediction Method: `argmax()` classification

---

## 📂 Project Structure

```
Brain-Tumor-Detection/
│
├── main.py
├── requirements.txt
├── runtime.txt
├── models/
│   └── model.h5
├── templates/
│   └── index.html
├── static/
├── uploads/
└── README.md
```

---

## ⚙ Installation

### 1️⃣ Clone the repository

```
git clone https://github.com/your-username/Brain-Tumor-Detection.git
cd Brain-Tumor-Detection
```

### 2️⃣ Create virtual environment

```
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Run the application

```
python main.py
```

Application will run at:

```
http://127.0.0.1:5000/
```

---

## 🌐 Deployment Configuration

The project is configured for production using:

```
gunicorn main:app --workers 1 --threads 1 --timeout 300
```

---

## 📸 Application Preview

### 🖥 Upload Interface

(Add screenshot inside `static/images/home.png`)

```
![Upload Page](static/images/home.png)
```

---

### 🔍 Prediction Output

(Add screenshot inside `static/images/output.png`)

```
![Prediction Output](static/images/output.png)
```

---

## 🚀 Key Features

- Clean UI design
- Real-time tumor classification
- Confidence score display
- Production-ready deployment setup
- Structured and modular project architecture

---

## 📈 Future Improvements

- Model optimization (TensorFlow Lite)
- Docker containerization
- REST API version
- Accuracy enhancement with larger dataset

---

## 👨‍💻 Author

Aditya Kumar  

Portfolio: https://aditya82.netlify.app/  
Email: adityasingh829442@gmail.com