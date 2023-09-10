from flask import Flask,render_template,redirect,request,url_for
import pickle


app=Flask(__name__)

model=pickle.load(open("RegressionFinal.pkl","rb"))
@app.route("/")
@app.route("/home")
def home():
    if request.method=='GET':
        return render_template("home.html")
    else:
        return redirect(url_for("prediction"))

@app.route("/prediction")
def prediction():
    name=request.form['country']
    year=request.form['year']
    predict=model.predict(name,year)
    return render_template("index.html",pre_text="predict")


if __name__=="__main__":
    app.run(debug=True)