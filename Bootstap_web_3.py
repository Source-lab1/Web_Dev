from flask import Flask , render_template

app = Flask(__name__, template_folder= 'template' )


@app.route('/')
def display():
    return render_template('Index_1.html')


@app.route("/bootstrap")
def boot():
    return render_template('bootstrap.html')

app.run(debug=True)
