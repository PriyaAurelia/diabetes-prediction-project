📌 Diabetes Prediction – End-to-End Data Science Project

📖 Project Description



This project is an end-to-end data science application that predicts whether a person has diabetes based on medical parameters.

The project covers the complete data science lifecycle including data collection, preprocessing, model training, evaluation, and deployment using a Flask API.



🛠️ Technologies Used



Python



Pandas



NumPy



Scikit-learn



Flask



📂 Project Structure



diabetes.csv – Dataset used for training the model



train\_model.py – Script for data preprocessing, model training, and saving the model



diabetes\_model.pkl – Trained machine learning model



app.py – Flask API for making predictions



⚙️ How It Works



The dataset is loaded and preprocessed.



A machine learning model is trained using scikit-learn.



The trained model is saved using pickle.



A Flask API is created to accept user input and return predictions.



The API predicts whether the person has diabetes or not.



🚀 How to Run the Project



Install required libraries:



pip install pandas numpy scikit-learn flask





Train the model:



python train\_model.py





Run the Flask app:



python app.py





Send a POST request to:



http://127.0.0.1:5000/predict



🎯 Outcome



The application successfully predicts diabetes based on input data and demonstrates a complete end-to-end data science workflow.



✨ This project was developed as part of an internship task to demonstrate practical data science and model deployment skills.

