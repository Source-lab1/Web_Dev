from flask import Flask


app =Flask(__name__)


@app.route('/')
def hello():
    return "Hello World"


@app.route('/nandesh')
def nandesh():
    return "Hello Nandesh , How are you , I  hope you are having a great day !!"

app.run(debug=True)