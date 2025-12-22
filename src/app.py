from flask import Flask, render_template, request
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

app = Flask(__name__)


df = pd.read_csv("data/data_final.csv")

X = df.drop(columns=["id", "decision_fatigue_level"])
X = X.apply(pd.to_numeric, errors="coerce")
X = X.dropna()
y = df.loc[X.index, "decision_fatigue_level"]


model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

label_map = {
    0: "Low Decision Fatigue",
    1: "Medium Decision Fatigue",
    2: "High Decision Fatigue"
}

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None

    if request.method == "POST":
        user_data = [[
            float(request.form["age"]),
            float(request.form["academic_pressure"]),
            float(request.form["work_pressure"]),
            float(request.form["cgpa"]),
            float(request.form["study_satisfaction"]),
            float(request.form["sleep_hours"]),
            float(request.form["work_study_hours"]),
            float(request.form["financial_stress"])
        ]]

        result = model.predict(user_data)[0]
        prediction = label_map[result]

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)

