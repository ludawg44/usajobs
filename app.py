from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)
# COMPLETE THIS NOW
# app.config['SQLALCHEMY_DATABASE_URI'] =

all_jobs = [
    {
        'title': 'Data Analyst',
        'salary': 100000,
        'city': 'New York',
        'state': 'New York',
        'security': 'secret'
    },
    {
        'title': 'Engineer',
        'salary': 105000,
        'city': 'Rochester',
        'state': 'New York'
    }
]

headers = {
    'User-Agent': 'veraluis4@gmail.com',
    'Authorization-Key': 'czWxB0/hvva4RLd9N6MNClvbek8igw12RjDOTZrQLiE='
}
ROOT_URL = 'https://data.usajobs.gov/'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/jobs')
def jobs():
    return render_template('jobs.html', jobs=all_jobs)

@app.route('/search/<string:keyword>')
def keyword_search(keyword):
    payload = {
        'Keyword': keyword,
    }
    response = requests.get(f"{ROOT_URL}/api/search?&",
                            params=payload,
                            headers=headers)
    return response.json()

# # Passing in a string name
# @app.route('/<string:name>')
# def name(name):
#     return "Hello, " + name

if __name__ == "__main__":
    app.run(debug=True)