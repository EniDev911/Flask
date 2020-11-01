from flask import Flask
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

db_connect = create_engine('sqlite:///mydatabase.db')
app = Flask(__name__)
api = Api(app)

class Robot(Resource):
    def get(self):
        conn = db_connect.connect() #Connect to database
        query = conn.execute("select * from robot")
@app.route("/")
def hello():
    return "hello world"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
