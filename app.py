from flask import Flask ,render_template, jsonify

app = Flask(__name__)

Jobs = [
  {
    'id': 1,
    'title': 'Front-end Engineer',
    'location': 'San-Francisco',
    'salary': '$120,000',
  },
  {
    'id': 2,
    'title': 'Back-end Engineer',
    'location': 'Delhi',
    'salary': '$150,000',
  },
  {
    'id': 3,
    'title': 'DevOps Engineer',
    'location': 'Noida',
    'salary': '$170,000',
  },
  {
    'id': 4,
    'title': 'Full-Stack Engineer',
    'location': 'Mumbai',
  }
]

@app.route("/")
def jobs_page():
  return render_template('home.html', jobs = Jobs, Company_name = 'Soft Micro')

@app.route("/api/jobs")
def jobs_api():
  return jsonify(Jobs)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
