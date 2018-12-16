import psycopg2
import datetime

def get_data():
    conn = psycopg2.connect("host= password= dbname= user=")
    cur = conn.cursor()
    cur.execute("SELECT user_id, add_date FROM users ORDER BY add_date;")
    return [[i, datetime.datetime.strftime(date, "%Y.%m.%d %H:%M:%S")] for i, date in cur.fetchall()]

#print(get_data())
