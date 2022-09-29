from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/login",methods=['GET'])
def login():
    return render_template("login.html")
@app.route("/do/reg")
def do_reg():

    # print(request.args)
    return render_template("index.html")

if __name__ == '__main__':
    app.run()