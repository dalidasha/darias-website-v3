from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Scientist',
        'location': 'Dehli, India',
        'salary': '67790',
    },
{
        'id': 2,
        'title': ' Scientist',
        'location': 'India',
        'salary': '10488',
    },
{
        'id': 3,
        'title': 'Data ',
        'location': 'Dehli',

    },
]

@app.route('/')
def hello_world():  # put application's code here
    return render_template('home.html', jobs=JOBS, company_name='advbgf')

@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)

