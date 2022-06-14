from flask import Flask
from flask_restful import Api, Resource, abort
from bfs4 import get_data
# from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)


#database
# db = SQLAlchemy(app)
api=Api(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'






# validate request
def notFound(symbol):
    if len(get_data(symbol)) == 1:
        abort(404, message="Not found")

# design
class Symbol(Resource):
    def get(self,symbol):
        notFound(symbol)
        info = get_data(symbol)
        return info
    def post(self,symbol):
        return {"data":"return data= "+ symbol}

# call
api.add_resource(Symbol, '/<string:symbol>')


if __name__ == '__main__':
    app.run(debug=True)

