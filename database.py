from sqlalchemy import create_engine, text
import os

connection_string = os.environ['db_conn']

engine = create_engine(connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})

    
def load_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(dict(row._mapping))
    return jobs

def load_id_job(id):
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs where id = :val"), {"val":id})
    row = result.all()
    if len(row)==0:
      return None
    else:
      return dict(row[0]._mapping)
print(load_id_job(1))