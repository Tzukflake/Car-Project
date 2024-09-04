from models import User, Car
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import db

class CarService:
    def __init__(self):
        engine = create_engine('sqlite:///instance/trafikverket.db')
        self.Session = sessionmaker(bind=engine)

    #hämtar alla bilar
    def get_all_cars(self):
        cars = db.session.query(Car).all()
        db.session.close()
        return cars
    
    #hämtar en specifik bil baserat på id
    def get_car_by_id(self, car_id):
        car = db.session.query(Car).filter_by(id=car_id).first()
        db.session.close()
        return car
    
    #skapar en ny bil
    def create_car(self, car_data):
        owner_id = car_data.pop('owner_id', None)
        car = Car(**car_data) #öppnar upp datan och skapar en ny bil med det
        if owner_id is not None:  # kollar om owner id finns
            car.owner_id = owner_id  # ger ett owner id till bilen
        db.session.add(car)
        db.session.commit()
        return car.id
    

    #uppdaterar en existerande bil där värdena sätts till null om dom inte uppdateras
    def update_car(self, car_id, car_data):
        car = Car.query.get(car_id)
        if car is None:
            return None
    
        #poppar ut id från datan då den inte ska bli uppdaterad
        car_data.pop('id', None)
    
        # uppdaterar bilens fält
        for field, value in car_data.items():
            setattr(car, field, value) # Använder setattr för att uppdatera bilens fält
    
        # specifikt sätter upp attributena för att se till att dom blir korrekt uppdaterade
        car.color = car_data.get('color')
        car.owner_id = car_data.get('owner_id')
        car.model_year = car_data.get('model_year')
        car.brand = car_data.get('brand')
        car.model_name = car_data.get('model_name')
        car.registration_plate = car_data.get('registration_plate')
    
        db.session.commit()
        return car
    
    #uppdaterar en existerande bil men om inte alla värden finns så behåller man de gamla
    def update_car_patch(self, car_id, car_data):
        car = Car.query.get(car_id)
        if car is None:
            return None
        
        for field, value in car_data.items():
            # Kontrollerar om fältet finns i Car-modellen innan uppdatering
            if hasattr(car, field):
                setattr(car, field, value) # Använder setattr för att uppdatera bilens fält

        db.session.commit()
        return car
    
    def delete_car(self, car_id):
        car = Car.query.get(car_id)
        if car:
            db.session.delete(car)
            db.session.commit()

class UserService:
    def __init__(self):
        engine = create_engine('sqlite:///instance/trafikverket.db')
        self.Session = sessionmaker(bind=engine)
    
    #hämtar alla användare
    def get_all_users(self):
        users = db.session.query(User).all()
        user_dicts = [{'id': user.id, 'first_name': user.first_name, 'last_name': user.last_name, 'personal_number': user.personal_number, 'address': user.address} for user in users]
        db.session.close()
        return user_dicts

    #hämtar en användare baserat på ett id
    def get_user_by_id(self, user_id):
        user = db.session.query(User).filter_by(id=user_id).first()
        db.session.close()
        return {'id': user.id, 'first_name': user.first_name, 'last_name': user.last_name, 'personal_number': user.personal_number, 'address': user.address}
    
    #skapar en användare
    def create_user(self, user_data):
        user = User(**user_data)
        db.session.add(user)
        db.session.commit()
        db.session.close()

    #uppdaterar en användare och om inte alla fält finns med så sätts de fälten till null
    def update_user(self, user_id, user_data):
        user = User.query.get(user_id)
        if user is None:
            return None

        #poppar ut id från datan för den ska inte behöva bli uppdaterad
        user_data.pop('id', None)

        # Updaterar user fälten
        for field, value in user_data.items():
            setattr(user, field, value)

        # specifikt sätter upp attributen för att se till att dom blir korrekt uppdaterade eller sätta till none
        user.first_name = user_data.get('first_name')
        user.last_name = user_data.get('last_name')
        user.personal_number = user_data.get('personal_number')
        user.address = user_data.get('address')

        db.session.commit()
        return user
    
    #uppdaterar en användare och om inte alla fält är med så behåller man dom gamla fälten
    def update_user_patch(self, user_id, user_data):
        user = User.query.get(user_id)
        if user is None:
            return None

        #poppar ut id från datan för den ska inte behöva bli uppdaterad
        user_data.pop('id', None)

        # Updaterar user fälten
        for field, value in user_data.items():
            setattr(user, field, value)

        db.session.commit()
        return user
    
    #tar bort en användare
    def delete_user(self, user_id):
        db.session.query(User).filter_by(id=user_id).delete()
        db.session.commit()
        db.session.close()

    
    


