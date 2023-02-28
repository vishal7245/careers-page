from sqlalchemy import create_engine
import os

connection_string = os.environ['db_conn']

engine = create_engine(connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


