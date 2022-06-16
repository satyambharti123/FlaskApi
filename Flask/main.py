from flask import Flask,redirect,url_for,render_template,request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/member")
def member():
    return "hello world is good"

@app.route("/sucess/<int:score>")
def sucess(score):
    res=""
    if score>35:
        res="PASS"
    else:
        res="FAIL"
    exp={'score':score,'res':res}        
    return render_template('result.html',result=exp)        

@app.route("/fail/<int:score>")
def fail(score):
    return "the person is fail and the marks is" + str(score)

@app.route("/result/<int:marks>")
def result(marks):
   result=""
   if marks>35:
       result="sucess"
   else:
        result="fail"
   return redirect(url_for(result,score=marks))


@app.route("/submit",methods=['POST','GET'])
def submit():
    total_score=0
    if request.method == 'POST':
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        physics=float(request.form['physics'])
        total_score=(maths+c+physics)/3
    res=""
   
    return redirect(url_for("sucess",score=total_score))            





if __name__ == '__main__':
    app.run()