from flask import Flask, request, render_template, url_for
import webScraper

app = Flask(__name__)
@app.route('/')
def getHomepage():
    return render_template('homepage.html')

@app.route('/', methods = ['POST'])
def process(): 
    text = request.form['text']
	canScrape = webScraper.findJS(text)
	if(canScrape == "error, invalid url")
	{
		return render_template('invalid_url.html')
	}
	else if(canScrape == "weird charSet")
	{
		return render_template('charSet.html')
	}
	else if(canScrape == "it has js")
	{
		return render_template('hasJS.html')
	}
	else
	{
		return render_template('noJS.html')
	}

app.run()
