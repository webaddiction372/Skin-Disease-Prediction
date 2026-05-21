# Skin Disease Prediction System

AI-powered web application for predicting skin diseases using Deep Learning.

---

## Features

- Skin disease prediction using AI
- Image upload support
- Deep Learning model integration
- Flask backend
- Responsive frontend
- Fast prediction results

---

## Technologies Used

### Frontend
- React
- HTML
- CSS
- JavaScript

### Backend
- Python
- Flask

### Machine Learning
- TensorFlow
- Keras
- OpenCV
- NumPy
- Pillow

---

## Project Structure

```bash
Skin-Disease-Prediction/
│
├── backend/
│   │
│   ├── app.py
│   ├── requirements.txt
│   ├── config.py
│   │
│   ├── models/
│   │   ├── skin_disease_model.keras
│   │   ├── labels.txt
│   │   └── model_loader.py
│   │
│   ├── utils/
│   │   ├── preprocess.py
│   │   ├── predict.py
│   │   └── helper.py
│   │
│   ├── routes/
│   │   ├── prediction_routes.py
│   │   └── api_routes.py
│   │
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   │
│   ├── templates/
│   │   ├── index.html
│   │   └── result.html
│   │
│   └── uploads/
│
├── frontend/
│   │
│   ├── public/
│   │
│   ├── src/
│   │   ├── assets/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── App.js
│   │   └── main.js
│   │
│   ├── package.json
│   ├── package-lock.json
│   └── vite.config.js
│
├── dataset/
│   ├── train/
│   ├── test/
│   └── validation/
│
├── notebooks/
│   └── model_training.ipynb
│
├── screenshots/
│
├── .gitignore
├── README.md
└── LICENSE
```

## Installation

### Clone Repository

```bash
git clone https://github.com/webaddiction372/Skin-Disease-Prediction.git
```

### Open Project Folder

```bash
cd Skin-Disease-Prediction
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Virtual Environment

#### Windows

```bash
.venv\Scripts\activate
```

#### Linux / Mac

```bash
source .venv/bin/activate
```

### Install Backend Dependencies

```bash
pip install -r requirements.txt
```

---

## Frontend Setup

### Move to frontend folder

```bash
cd frontend
```

### Install dependencies

```bash
npm install
```

### Run frontend

```bash
npm run dev
```

or

```bash
npm start
```

---

## Run Backend

Move back to root folder:

```bash
cd ..
```

Run Flask server:

```bash
python app.py
```

---

## How It Works

1. Upload skin image
2. Image preprocessing
3. Model prediction
4. Display result

---

## Supported Formats

- JPG
- JPEG
- PNG

---

## Future Improvements

- More disease categories
- Better accuracy
- Mobile application
- Doctor consultation feature

---

## Disclaimer

This project is for educational purposes only and should not be considered medical advice.

---

## Author

### Nitin Singh

## License

MIT License
