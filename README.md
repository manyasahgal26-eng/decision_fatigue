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



## Machine Learning Used
- Algorithm: Decision Tree Classifier  
- Overfitting handled using:
  - limited tree depth  
  - minimum samples per split  
  - class balancing  
- Accuracy is checked using a train-test split  



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



