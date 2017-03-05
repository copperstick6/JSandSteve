from flask import Flask, request, render_template, url_for

app = Flask(__name__)
@app.route('/')
def getHomepage():
    return render_template('homepage.html')

@app.route('/', methods = ['POST'])
def process():
    text = request.form['text']
    return text

app.run()
