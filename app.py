from flask import Flask, render_template, request
import pickle
import numpy as np
# Load the Random Forest CLassifier model
filename = 'random_forest_model.pkl'
model = pickle.load(open (filename, 'rb'))
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('main.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        # Get input values from the form
        try:
            Height = int(request.form['Height'])
            Weight = int(request.form['Weight'])
            High_Cholesterol = int(request.form['High_Cholesterol'])
            Blood_Pressure = int(request.form['Blood_Pressure'])
            Mental_Health = int(request.form['Mental_Health'])  
            Physical_Health = int(request.form['Physical_Health'])
            Smoking_Habit = int(request.form['Smoking_Habit'])
            Exercise = int(request.form['Exercise'])
            sex = int(request.form['sex'])
            age = int(request.form['age'])
            Drinking_Habit_ord = int(request.form['Drinking_Habit_ord'])
            Water_Habit_ord  = int(request.form['Water_Habit_ord'])
            Fruit_Habit_ord = int(request.form['Fruit_Habit_ord'])
            Diabetes_ord = int(request.form['Diabetes_ord'])
            Checkup_ord = int(request.form['Checkup_ord'])
        except:
            return render_template('error.html', message='Invalid input values')
        
            # Prepare input data for prediction
        data = np.array([Height,Weight,High_Cholesterol,Blood_Pressure,Mental_Health,Physical_Health,Smoking_Habit, Exercise, sex, age, Drinking_Habit_ord,Water_Habit_ord,Fruit_Habit_ord,Diabetes_ord,Checkup_ord])
        data = data.reshape(1, -1)
        # Make prediction and display result
        my_prediction = model.predict(data)
        return render_template('result.html', prediction=my_prediction)
    else:
        return render_template('error.html', message='No input values provided')



if __name__ == '__main__':
    app.run(debug=True)
