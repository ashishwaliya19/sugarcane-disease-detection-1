# 🌿 Sugarcane Disease Detection using Deep Learning

![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square&logo=python)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.19-orange?style=flat-square&logo=tensorflow)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?style=flat-square&logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Model](https://img.shields.io/badge/Model-Git%20LFS-purple?style=flat-square)

🔗 **Live Demo:** [sugarcane-disease-detection.streamlit.app](https://sugarcane-disease-detection-1-qudzotjyn8ngmokkatcev6.streamlit.app)

---

## 📌 Project Overview

An **image-based machine learning system** for the automated detection, classification, and identification of sugarcane leaf diseases. This project leverages a **Convolutional Neural Network (CNN)** model trained on sugarcane leaf images to accurately distinguish between healthy and diseased crops, helping farmers take timely action to prevent yield loss.

The system is deployed via a **Streamlit web application**, enabling users to upload leaf images and receive instant disease predictions.

---

## ✨ Features

- 🔍 **Automated Disease Detection** – Upload a leaf image and get an instant diagnosis
- 🧠 **Deep Learning Classification** – CNN model trained on real sugarcane leaf datasets
- 🌾 **Multi-Class Disease Identification** – Detects 5 categories including healthy leaves
- 📊 **Confidence Score** – Displays prediction confidence for each classification
- 🖥️ **Interactive Web Interface** – Simple and intuitive Streamlit-based UI
- ⚡ **Fast Inference** – Real-time predictions with minimal latency

---

## 🦠 Diseases Detected

| Class | Description |
|-------|-------------|
| ✅ **Healthy** | No disease detected — normal leaf |
| 🔴 **Red Rot** | Caused by *Colletotrichum falcatum*; red discoloration inside stalks |
| 🟤 **Rust** | Caused by *Puccinia melanocephala*; orange-brown pustules on leaves |
| 🟡 **Yellow** | Yellowing of leaves due to nutrient deficiency or viral infection |
| 🟣 **Mosaic** | Viral disease causing mosaic-like discoloration patterns on leaves |

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| Language | Python 3.11 |
| Deep Learning | TensorFlow 2.19 / Keras |
| Model Architecture | Convolutional Neural Network (CNN) |
| Web Application | Streamlit |
| Image Processing | OpenCV / PIL |
| Model Storage | Git LFS (.h5 format) |
| Deployment | Streamlit Cloud |

---

## 📁 Project Structure

```
sugarcane-disease-detection/
│
├── app.py                    # Streamlit web application
├── train.py                  # Model training script
├── predict.py                # Prediction/inference script
├── sugarcane_model.h5        # Trained CNN model (stored via Git LFS)
├── requirements.txt          # Python dependencies
├── runtime.txt               # Python version (3.11)
├── .gitattributes            # Git LFS tracking config
└── README.md                 # Project documentation
```

---

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.11
- Git LFS installed (`git lfs install`)
- pip package manager

### Steps

**1. Clone the repository**
```bash
git clone https://github.com/ashishwaliya19/sugarcane-disease-detection-1.git
cd sugarcane-disease-detection-1
```

**2. Pull the model file via Git LFS**
```bash
git lfs pull
```

**3. Create and activate virtual environment**
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

**4. Install dependencies**
```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

### Running the Web Application
```bash
streamlit run app.py
```
Open browser at `http://localhost:8501`

### Training the Model
```bash
python train.py
```

### Running Predictions via Script
```bash
python predict.py --image path/to/leaf_image.jpg
```

### How to Use the Web App
1. Launch the Streamlit app
2. Click **"Browse files"** to upload a sugarcane leaf image (JPG/PNG)
3. View the **predicted disease class** and **confidence score**

---

## 🧪 Model Details

- **Architecture:** Convolutional Neural Network (CNN)
- **Input Size:** 224 × 224 × 3 (RGB images)
- **Output Classes:** 5 (Healthy, RedRot, Rust, Yellow, Mosaic)
- **Framework:** TensorFlow 2.19 / Keras
- **Saved Format:** `.h5` (stored via Git LFS)

---

## 🌐 Deployment

This app is deployed on **Streamlit Cloud** with the following configuration:

- **Python Version:** 3.11 (set via `runtime.txt`)
- **Model:** Stored in repository via **Git LFS**
- **Live URL:** [Click here to open app](https://sugarcane-disease-detection-1-qudzotjyn8ngmokkatcev6.streamlit.app)

---

## 🤝 Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---



---

## 👨‍💻 Author

**Ashish Kumar**
Developed as part of a research project on image-based machine learning for agricultural disease detection.

---

> ⭐ If you found this project helpful, please give it a star!