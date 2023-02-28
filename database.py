from sqlalchemy import create_engine

connection_string = "mysql+pymysql://7wjo3odm9zfzg2cp8juv:pscale_pw_LNzYqO1W9TUumLgNknzs1OQAwPtxYhz2SI0mLb8vPmP@ap-south.connect.psdb.cloud/career-db?charset=utf8mb4"

engine = create_engine(connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


