from db.utils import connect_to_db
from slugify import slugify
import psycopg2.extras
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

def retrieve_info():#index=None):
    dict_list = []
    connection = connect_to_db()
    cursor = connection.cursor()
    #cursor = connection.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
    
    try:
        cursor.execute('SELECT title, contents, cover_url, author, image_url from blogs order by blog_id desc limit 9')
        query_res = cursor.fetchall()
        print(query_res)
    #    print('query_res')
    except Exception as e:
        print(e)
        query_res = None
    for item in query_res:
        tmp = {'title':item[0], 
        'contents' :item[1], 
        'cover_url':item[2], 
        'author':item[3],
        'image_url':item[4]
        }
        dict_list.append(tmp)

    return dict_list

#check
#print(retrieve_info())