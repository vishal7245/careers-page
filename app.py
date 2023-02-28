from flask import Flask ,render_template, jsonify
from database import engine
from sqlalchemy import text

app = Flask(__name__)

def load_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(dict(row._mapping))
    return jobs
    

@app.route("/")
def jobs_page():
  Jobs = load_db()
  return render_template('home.html', jobs = Jobs, Company_name = 'Soft Micro')

@app.route("/api/jobs")
def jobs_api():
  return jsonify(load_db())


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
