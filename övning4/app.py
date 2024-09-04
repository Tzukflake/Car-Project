from flask import Flask, jsonify, request, Response
from services import CarService, UserService
from models import db, User
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///trafikverket.db'

db.init_app(app)

#skapar databastabellerna
with app.app_context():
    db.create_all() 

car_service = CarService()
user_service = UserService()

#endpoints för cars

#hämtar alla bilar
@app.route('/cars/', methods=['GET'])
def get_all_cars():
    cars = car_service.get_all_cars()
    cars_data = []
    for car in cars:
        #plockar ut ägaren för bilarna baserat på ägar id
        owner_id = car.owner_id
        owner = User.query.get(car.owner_id) if car.owner_id else None
        if owner:
            owner_info = {
                'owner_id': owner_id,
                'first_name': owner.first_name,
                'last_name': owner.last_name,
                'personal_number': owner.personal_number,
                'address': owner.address
            }
        else:
            owner_info = None
        #plockar ut bil infon
        car_info = {
            'id': car.id,
            'brand': car.brand,
            'model_name': car.model_name,
            'model_year': car.model_year,
            'color': car.color,
            'registration_plate': car.registration_plate,
            'owner_info': owner_info
        }
        cars_data.append(car_info)
   #konverterar listan med dicts till json med sorterade nycklar
    json_data = json.dumps(cars_data, ensure_ascii=False, indent=4, sort_keys=False)
    
    # Return en flask response och sätter datat specifikt till json
    return Response(response=json_data, status=200, mimetype="application/json")

#hämtar ut en specifik bil baserat på id
@app.route('/cars/<int:car_id>/', methods=['GET'])
def get_car(car_id):
    car = car_service.get_car_by_id(car_id)
    if not car:
        return jsonify({'error': 'Car not found'}), 404
    
    owner = User.query.get(car.owner_id)
    owner_info = None
    if owner:
        owner_info = {
            'owner_id': owner.id,
            'first_name': owner.first_name,
            'last_name': owner.last_name,
            'personal_number': owner.personal_number,
            'address': owner.address
        }
    
    car_info = {
        'id': car.id,
        'brand': car.brand,
        'model_name': car.model_name,
        'model_year': car.model_year,
        'color': car.color,
        'registration_plate': car.registration_plate,
        'owner_id': car.owner_id,
        'owner_info': owner_info
    }
    #konverterar variablen til en sorterad json
    json_data = json.dumps(car_info, ensure_ascii=False, indent=4, sort_keys=False)
    
    # Return en flask response och sätter datat specifikt till json
    return Response(response=json_data, status=200, mimetype="application/json")

#uppdaterar ett eller flera fält hos en bil, det som inte uppdateras blir null
@app.route('/cars/<int:car_id>/', methods=['PUT'])
def update_car(car_id):
    car_data = request.json
    car_service.update_car(car_id, car_data)
    return '', 200

#uppdaterar en eller flera fält hos en bil, det som inte uppdateras behåller sitt värde
@app.route('/cars/<int:car_id>/', methods=['PATCH'])
def patch_car(car_id):
    car_data = request.json
    car_service.update_car_patch(car_id, car_data)
    return '', 200


#tar bort en bil
@app.route('/cars/<int:car_id>/', methods=['DELETE'])
def delete_car(car_id):
    car_service.delete_car(car_id)
    return '', 204

#skapar en ny bil som blir kopplat till en ägare
@app.route('/cars/', methods=['POST'])
def create_car():
    car_data = request.json
    car_id = car_service.create_car(car_data)
    car = car_service.get_car_by_id(car_id)
    
    car_info = {
        'id': car.id,
        'brand': car.brand,
        'model_name': car.model_name,
        'model_year': car.model_year,
        'color': car.color,
        'registration_plate': car.registration_plate,
        'owner_id': car.owner_id,  
    }
    
    return jsonify(car_info), 201

#användar endpoints

#hämtar alla användare
@app.route('/users/', methods=['GET'])
def get_all_users():
    users = user_service.get_all_users()
    return jsonify(users)

#hämtar en specifik användare
@app.route('/users/<int:user_id>/', methods=['GET'])
def get_user(user_id):
    user = user_service.get_user_by_id(user_id)
    return jsonify(user)

#skapar en ny användare
@app.route('/users/', methods=['POST'])
def create_user():
    user_data = request.json
    user_service.create_user(user_data)
    return '', 201

#uppdaterar ett eller flera fält hos en användare, det som inte uppdateras blir null
@app.route('/users/<int:user_id>/', methods=['PUT'])
def update_user(user_id):
    user_data = request.json
    user_service.update_user(user_id, user_data)
    return '', 200

#uppdaterar ett eller flera fält hos en användare, det som inte uppdateras behåller tidigare data
@app.route('/users/<int:user_id>/', methods=['PATCH'])
def patch_user(user_id):
    user_data = request.json
    user_service.update_user_patch(user_id, user_data)
    return '', 200

#tar bort en användare
@app.route('/users/<int:user_id>/', methods=['DELETE'])
def delete_user(user_id):
    user_service.delete_user(user_id)
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)