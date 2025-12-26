# Decision Fatigue Predictor

This project predicts decision fatigue level (Low / Medium / High) using basic academic and lifestyle data.  
It uses a machine learning model and a simple Flask web application.



## What is this project?
Students often feel mentally tired because of:
 academic pressure
 lack of sleep
 long study/work hours
 financial stress  

This project takes such inputs and predicts the level of decision fatigue.



## Features
- Takes user input through a web form  
- Predicts decision fatigue using ML  
- Shows result as Low / Medium / High  
- If fatigue is **High**, redirects to the **Tele MANAS mental health support website**  
- Simple UI using HTML and CSS  



Supervised Learning: Used because the dataset contains labeled decision fatigue levels.
Classification: Used to categorize fatigue into Low, Medium, and High.
Data Preprocessing: Used to clean and convert raw input data into numerical form.
Feature Selection: Used to keep only relevant factors affecting decision fatigue.
Train–Test Split: Used to evaluate the model on unseen data.
Decision Tree Classifier: Used for its simplicity and effectiveness on tabular data.
Overfitting Control: Used to prevent the model from memorizing the data.
Class Imbalance Handling: Used to avoid bias toward dominant classes.
Model Evaluation (Accuracy): Used to measure model performance.
Rule-based Post Processing: Used to make predictions more realistic and stable. 



## Tech Stack
- Python  
- Pandas  
- Scikit-learn  
- Flask  
- HTML & CSS  



to run use the following command in terminal
python3 src/app.py
to check model accuracy
python3 src/decision_fatigue_model.py

<img width="605" height="215" alt="image" src="https://github.com/user-attachments/assets/792a49c4-bb7d-4743-9f03-9c841e28c61f" />
<img width="909" height="553" alt="image" src="https://github.com/user-attachments/assets/2e155ccf-f22a-48fa-9249-60e2fba4db27" />
<img width="908" height="545" alt="image" src="https://github.com/user-attachments/assets/3c457502-d5a5-4ae5-8798-2d563246eaf8" />
<img width="913" height="546" alt="image" src="https://github.com/user-attachments/assets/b6cf0408-6887-46ca-9c8f-9400d98fb182" />
by clicking on professional help , we get directed to https://telemanas.mohfw.gov.in/home 





