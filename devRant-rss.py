from flask import Flask, render_template, make_response
import requests

app = Flask(__name__)
url = "https://www.devrant.io/api/devrant/rants?app=3"

@app.route('/')
def index():
    rants = requests.get(url).json()['rants']
    xml_feed = render_template('feeds.xml', rants=rants)
    response = make_response(xml_feed)
    response.headers['Content-Type'] = "application/xml"
    return response

if __name__ == '__main__':
    app.run(debug=True)
