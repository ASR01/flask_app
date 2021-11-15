import psycopg2
from dotenv import load_dotenv
import os

config = load_dotenv()
#print(config)
load_dotenv()

DBHOST = os.environ.get("DBHOST")
DBNAME= os.environ.get("DBNAME")
DBUSER= os.environ.get("DBUSER")
DBPASSWORD= os.environ.get("DBPASSWORD")

#print(DBHOST, DBNAME, DBUSER, DBPASSWORD)

def connect_to_db():
    try:
        conn = psycopg2.connect("dbname={} user={} host={} password={}".format(DBNAME,DBUSER,DBHOST,DBPASSWORD))
        print("connection is successfull")
        return conn
    except Exception as e:
        print(e)
        raise Exception("I am unable to connect to the database")
