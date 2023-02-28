from flask import Flask ,render_template, jsonify
from database import load_db, load_id_job

app = Flask(__name__)

@app.route("/")
def jobs_page():
  Jobs = load_db()
  return render_template('home.html', jobs = Jobs, Company_name = 'Soft Micro')

@app.route("/api/jobs")
def jobs_api():
  return jsonify(load_db())

@app.route("/job/<id>")
def show_job(id):
  job = load_id_job(id)
  if not job:
    return "Not Found", 404
  return render_template('job-page.html', job = job, Company_name = 'Soft Micro')

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
  