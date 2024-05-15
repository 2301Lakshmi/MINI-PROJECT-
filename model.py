from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class register(db.Model):
    __tablename__='register'
    Username=db.Column(db.VARCHAR,primary_key=True)
    Password=db.Column(db.VARCHAR)

class pets(db.Model):
    __tablename__='pets'
    Pet_id=db.Column(db.Integer,primary_key=True)
    pet_name=db.Column(db.VARCHAR)

class food(db.Model):
    __tablename__='food'
    food_id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    Pet_id=db.Column(db.Integer,db.ForeignKey("pets.Pet_id"))
    item=db.Column(db.VARCHAR)
    location=db.Column(db.VARCHAR)
    info=db.Column(db.VARCHAR)
    stock=db.Column(db.Integer)

class clothes(db.Model):
    __tablename__='clothes'
    Pet_id=db.Column(db.Integer,db.ForeignKey("pets.Pet_id"))
    cloth_id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    cloth=db.Column(db.VARCHAR)
    location=db.Column(db.VARCHAR)
    info=db.Column(db.VARCHAR)
    stock=db.Column(db.Integer)


class shelter(db.Model):
    __tablename__='shelter'
    shelter_id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    Pet_id=db.Column(db.Integer,db.ForeignKey("pets.Pet_id"))
    stay_item=db.Column(db.VARCHAR)
    location=db.Column(db.VARCHAR)
    info=db.Column(db.VARCHAR)
    stock=db.Column(db.Integer)

class admin(db.Model):
    __tablename__='admin'
    Username=db.Column(db.VARCHAR,primary_key=True)
    Password=db.Column(db.VARCHAR)



