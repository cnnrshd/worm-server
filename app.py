# app.py
from flask import Flask, request, g
import sqlite3
import datetime
app = Flask(__name__)
DATABASE = 'database.db'
INIT = "create table nodes(to, from, date)"
DB = None

def get_db():
    global DB
    if DB is None:
        DB = sqlite3.connect(DATABASE)
    return DB

# def init_db():
#     # with app.app_context():
#     db = get_db()
#     db.cursor().execute(INIT)
#         # with app.open_instance_resource('schema.sql', mode='r') as f:
#         #     db.cursor().executescript(f.read())
#         # db.commit()
#     db.commit()
#     db.close()

@app.route('/')
def hello_world():
    return "Hello world!"

@app.route('/w.js')
def return_worm():
    return "a javascript worm will be here eventually"

@app.route('/testing')
def return_testing():
    return "Unique value for testing: tsta3"

@app.route('/add')
def add_connection():
    frm = request.args.get('from')
    to = request.args.get('to')
    if frm and to:
        # add to db
        cur = get_db().cursor()
        sql = 'INSERT INTO nodes(to, from, date) VALUES(?,?,?);'
        val = (to, frm, datetime.datetime.now())
        cur.execute(sql, val)
        cur.commit()
        db.close()
        return "adding " + str(frm) + " " + str(to)
    else: 
        return "error adding to db"

@app.before_first_request
def init_db():
    # with app.app_context():
    db = get_db()
    db.cursor().execute(INIT)
    db.commit()
    db.close()

if __name__ == '__main__':
    init_db()
    # cur = get_db().cursor()
    # cur.execute(INIT)
    # cur.commit()
    print(a)
    app.run(host='0.0.0.0')