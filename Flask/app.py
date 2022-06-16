from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "HELLO WORLD"

@app.route("/member")
def member():
    return "hello world is good"

@app.route("/sucess/<int:score>")
def sucess(score):
    return "the person is passed and the marks is" + str(score)

@app.route("/fail/<int:score>")
def fail(score):
    return "the person is fail and the marks is" + str(score)

@app.route("/result/<int:marks>")
def result(marks):
   result=""
   if marks<35:
       result="fail"
   else:
        result="sucess"
   return redirect(url_for(result,score=marks))

 
           




if __name__ == '__main__':
    app.run()