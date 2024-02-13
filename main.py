from flask import Flask, render_template, request,jsonify
import matplotlib

import joblib

matplotlib.use('Agg')

DEFAULT_Male = 'Male'
DEFAULT_Age = 33
DEFAULT_CigsPerDay = 30
DEFAULT_TotChol = 22
DEFAULT_SysBP =161
DEFAULT_Glucose = 77

app = Flask(__name__)


@app.before_request
def start():
    global logreg
    logreg = joblib.load('logreg.joblib')


@app.route("/", methods=['POST', 'GET'])
def submit_new_profile():
    model_plot=''
    if(request.method=='POST'):
        Gender1= 1 if (request.form['selected_Male']=='Male') else 0
        Gender=request.form['selected_Male']
        Age=int(request.form['selected_Age'])
        CigsPerDay = int(request.form['selected_CigsPerDay'])
        TotChol = float(request.form['selected_TotChol'])
        SysBP=float(request.form['selected_SysBP'])
        Glucose=float(request.form['selected_Glucose'])

        new_features=[[Gender1,Age,CigsPerDay,TotChol,SysBP,Glucose]]

        model_plot=logreg.predict(new_features)
        if model_plot==0:
            model_plot='the person is not'
        else:
            model_plot='the person is likely'
        return render_template('index.html',model_plot=model_plot,selected_Male=Gender,selected_Age=Age,selected_CigsPerDay=CigsPerDay,selected_TotChol=TotChol,selected_SysBP=SysBP,selected_Glucose=Glucose)
    else:
        return render_template('index.html',model_plot="",selected_Male=DEFAULT_Male,selected_Age=DEFAULT_Age,selected_CigsPerDay=DEFAULT_CigsPerDay,selected_TotChol=DEFAULT_TotChol,selected_SysBP=DEFAULT_SysBP,selected_Glucose=DEFAULT_Glucose)







if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
