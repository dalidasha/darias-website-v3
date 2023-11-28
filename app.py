import os

from flask import Flask, render_template, jsonify
from database import load_jobs_from_db

app = Flask(__name__)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))

@app.route('/')
def hello_world():  # put application's code here
    jobs = load_jobs_from_db()
    return render_template('home.html', jobs=jobs, company_name='advbgf')

@app.route('/api/jobs')
def list_jobs():
    jobs = load_jobs_from_db()
    return jsonify(jobs)