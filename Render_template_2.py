from flask import Flask , render_template

app = Flask(__name__, template_folder= 'template' )

@app.route('/')
def display():
    return render_template('Index_1.html')


# @app.route("/about")
# def about():
#     return render_template('about_1.html')


# @app.route("/about")
# def about():
#     name = "Nandesh"
#     return render_template('about_1.html',name= name)

app.run(debug=True)
