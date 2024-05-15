from flask_restful import Resource
from model import db,register,admin,food,clothes,shelter
from flask import request,jsonify


class signup(Resource):
    def post(self):
        data = request.json  
        name  = data['name']
        password = data['password']
        users=register.query.all()
        flag=True
        for user in users:
            if name==user.Username:
               flag=False
        if(flag):
            obj=register(Username=name,Password=password)
            db.session.add(obj)
            db.session.commit()
            msg='Sign-Up Successful'
            return jsonify(msg)
        else:
            msg='Unsucessfull!!! Try again with a different username'
            return jsonify(msg)
        
class login(Resource):
    def post(self):
        data=request.json
        name  = data['name']
        password = data['password']
        users=register.query.all()
        flag=False
        for user in users:
            if name==user.Username and password==user.Password:
               flag=True
        if(flag):
            return '',200
        else:
            msg="Invalid Login"
            return jsonify(msg),401 
        
class AdminLogin(Resource):
    def post(self):
        data=request.json
        password = data['password']
        users=admin.query.all()
        flag=False
        for user in users:
            if password==user.Password:
               flag=True
        if(flag):
            return '',200
        else:
            msg="Invalid Login"
            return jsonify(msg),401 
        
class updatefoodstock(Resource):
     def put(self, id):
        data = request.json
        stock = data.get('stock')
        food_item = food.query.filter_by(food_id=id).first()
        food_item.stock = stock
        db.session.commit()

class updateclothstock(Resource):
     def put(self, id):
        data = request.json
        stock = data.get('stock')
        cloth_item = clothes.query.filter_by(cloth_id=id).first()
        cloth_item.stock = stock
        db.session.commit()

class updatestaystock(Resource):
     def put(self, id):
        data = request.json
        stock = data.get('stock')
        stay_item = shelter.query.filter_by(shelter_id=id).first()
        stay_item.stock = stock
        db.session.commit()

        
        



