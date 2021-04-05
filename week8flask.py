from flask import Flask, jsonify, abort, request
from sqlalchemy import create_engine #sqlalchemy helped convert strings to dates seamlessly
import mysql.connector as mysql
import pandas as pd

app = Flask(__name__)
db = mysql.connect(
    host = "db",
    user = "root",
    passwd = "root",
    db = "db"
)

@app.route('/links/', methods=['GET'])
def getlinks():
    cur = db.cursor()
    query = 'select * from linksdemo'
    cur.execute(query)
    print('TABLE COLUMS: ', cur.column_names, '\n')
    
    myresult = cur.fetchall()
    
    for x in myresult:
        print(x)
    return jsonify(myresult)




@app.route('/links/', methods=['POST'])
def create_link(dbalink):
    con_str = "mysql+mysqlconnector://root:root@db/db"
    engine = create_engine(con_str)
    df = pd.DataFrame({'Links': dbalink}, index = [-1])
    df = df.applymap(str)
    df.to_sql('linksdemo',con=engine, if_exists='append', index = False)

if __name__ == '__main__':
    app.run(debug=True)