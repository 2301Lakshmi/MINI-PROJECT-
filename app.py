from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from model import db
from controllers import signup,login,AdminLogin,updatefoodstock,updateclothstock,updatestaystock
from display_first import display_first_clothes,display_first_food,display_first_stay

app=Flask(__name__)

CORS(app, resources={r'/*': {'origins': "*"}},CORS_SUPPORTS_CREDENTIALS = True)
app.config['CORS_HEADERS'] = 'Content-Type'

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://root:Sadhu2407@localhost:3306/pet_db"
db.init_app(app)

api=Api(app)

api.add_resource(display_first_food,'/displayfood')
api.add_resource(display_first_clothes,'/displaycloth')
api.add_resource(display_first_stay,'/displaystay')
api.add_resource(signup,'/signup')
api.add_resource(login,'/login')
api.add_resource(AdminLogin,'/adminlogin')
api.add_resource(updatefoodstock,'/updatefoodstock/<int:id>')
api.add_resource(updateclothstock,'/updateclothstock/<int:id>')
api.add_resource(updatestaystock,'/updatestaystock/<int:id>')


if __name__ == '__main__':
      app.run(debug=True)