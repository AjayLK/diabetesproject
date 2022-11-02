

from flask import Flask, jsonify, render_template, request
from diabetes_model.utils import DiabetesDisease
import config

app = Flask(__name__)

@app.route('/')
def hello_flask():
    print("Welcome")
    return render_template("index.html")

@app.route('/predicted_diabetes',methods = ['GET','POST'])
def get_heart_disease():
    if request.method == 'GET':
        print('we are using Get method')
    
        data = request.form
        print("Data-->",data)

        Glucose = eval(request.args.get('Glucose'))
        BloodPressure = eval(request.args.get('Glucose'))
        SkinThickness = eval(request.args.get('Glucose'))
        Insulin = eval(request.args.get('Glucose'))
        BMI = eval(request.args.get('Glucose'))
        DiabetesPedigreeFunction = eval(request.args.get('Glucose'))
        Age = eval(request.args.get('Glucose'))

        print('Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age',Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age)

        dd = DiabetesDisease(Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age)
        disease = dd.get_predicted_disease()
        if disease == 0:
            return render_template("index.html", prediction='The patient has no symptoms of diabetes,he is well.')
        else:
            return render_template("index.html", prediction='The patient has symptoms of diabetes,he should seek treatment.')

    else: 
        print('we are using Post method')
    
        data = request.form
        print("Data-->",data)

        Glucose = eval(request.form.get('Glucose'))
        BloodPressure = eval(request.form.get('Glucose'))
        SkinThickness = eval(request.form.get('Glucose'))
        Insulin = eval(request.form.get('Glucose'))
        BMI = eval(request.form.get('Glucose'))
        DiabetesPedigreeFunction = eval(request.form.get('Glucose'))
        Age = eval(request.form.get('Glucose'))

        print('Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age',Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age)

        dd = DiabetesDisease(Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age)
        disease = dd.get_predicted_disease()
        if disease == 0:
            return render_template("index.html", prediction='The patient has no symptoms of diabetes,he is well.')
        else:
            return render_template("index.html", prediction='The patient has symptoms of diabetes,he should seek treatment.')


  

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = config.PORT_NUMBER, debug = True)