from model import food, shelter,clothes,pets,db
from flask_restful import Resource
import json 
from flask import request,jsonify

class display_first_food(Resource):
    def get(self):
        food_data = {}
        foods = food.query.all()
        for food_item in foods:
            pet = pets.query.filter_by(Pet_id=food_item.Pet_id).first()
            name=pet.pet_name
            food_data[food_item.food_id] = {
                'name': food_item.item,
                'location': food_item.location,
                'pet': name,
                'info': food_item.info,
                'stock': food_item.stock,
                'food_id': food_item.food_id
            }
        return jsonify(food_data)

    def post(self):
        data=request.get_json()
        if data.get('pet')=="Dog":
            num=1
        elif data.get('pet')=="Cat":
            num=2
        else:
            num=3
        obj=food(Pet_id=num,item=data.get('name'),location=data.get('loc'),info=data.get('des'),stock=data.get('stock'))
        db.session.add(obj)
        db.session.commit()

class display_first_clothes(Resource):
     def get(self):
        cloth_data = {}
        cloths = clothes.query.all()
        for cloth_item in cloths:
            pet = pets.query.filter_by(Pet_id=cloth_item.Pet_id).first()
            name=pet.pet_name
            cloth_data[cloth_item.cloth_id] = {
                'name': cloth_item.cloth,
                'location': cloth_item.location,
                'pet': name,
                'info': cloth_item.info,
                'stock': cloth_item.stock,
                'cloth_id': cloth_item.cloth_id
            }
        return jsonify(cloth_data)
     
     def post(self):
        data=request.get_json()
        if data.get('pet')=="Dog":
            num=1
        elif data.get('pet')=="Cat":
            num=2
        else:
            num=3
        obj=clothes(Pet_id=num,cloth=data.get('name'),location=data.get('loc'),info=data.get('des'),stock=data.get('stock'))
        db.session.add(obj)
        db.session.commit()
    

class display_first_stay(Resource):
     def get(self):
        stay_data = {}
        stays = shelter.query.all()
        for stay_item in stays:
            pet = pets.query.filter_by(Pet_id=stay_item.Pet_id).first()
            name=pet.pet_name
            stay_data[stay_item.shelter_id] = {
                'name': stay_item.stay_item,
                'location': stay_item.location,
                'pet': name,
                'info': stay_item.info,
                'stock': stay_item.stock,
                'stay_id': stay_item.shelter_id
            }
        return jsonify(stay_data)
    
     def post(self):
        data=request.get_json()
        if data.get('pet')=="Dog":
            num=1
        elif data.get('pet')=="Cat":
            num=2
        else:
            num=3
        obj=shelter(Pet_id=num,stay_item=data.get('name'),location=data.get('loc'),info=data.get('des'),stock=data.get('stock'))
        db.session.add(obj)
        db.session.commit()
       


       