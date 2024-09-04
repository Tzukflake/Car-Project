from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import db, User, Car

engine = create_engine('sqlite:///instance/trafikverket.db')
db.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# skapar användare
users_data = [
    {"first_name": "Alice", "last_name": "Smith", "personal_number": "19850210-1234", "address": "123 Main St, Anytown"},
    {"first_name": "Bob", "last_name": "Johnson", "personal_number": "19780315-5678", "address": "456 Elm St, Othertown"},
    {"first_name": "Charlie", "last_name": "Brown", "personal_number": "19901025-9012", "address": "789 Oak St, Another Town"},
    {"first_name": "David", "last_name": "Lee", "personal_number": "19821205-3456", "address": "246 Pine St, Yet Another Town"},
    {"first_name": "Emma", "last_name": "Davis", "personal_number": "19950530-7890", "address": "135 Cedar St, Somewhere"},
    {"first_name": "Frank", "last_name": "Wilson", "personal_number": "19720418-2345", "address": "579 Birch St, Nowhere"},
    {"first_name": "Grace", "last_name": "Martinez", "personal_number": "19890608-6789", "address": "357 Maple St, Anywhere"},
    {"first_name": "Henry", "last_name": "Taylor", "personal_number": "19760120-1234", "address": "468 Walnut St, Elsewhere"},
    {"first_name": "Isabella", "last_name": "Anderson", "personal_number": "19981003-5678", "address": "579 Pine St, Nowhere"},
    {"first_name": "Jack", "last_name": "Garcia", "personal_number": "19831015-9012", "address": "246 Cedar St, Yet Another Town"}
]

for user_data in users_data:
    user = User(**user_data)
    session.add(user)

session.commit()

# skapar bilar
cars_data = [
    {"brand": "Volvo", "model_name": "XC60", "model_year": "2020", "color": "Black", "registration_plate": "ABC123", "owner_id": 1},
    {"brand": "Toyota", "model_name": "Camry", "model_year": "2018", "color": "Blue", "registration_plate": "DEF456", "owner_id": 2},
    {"brand": "Honda", "model_name": "Accord", "model_year": "2019", "color": "Red", "registration_plate": "GHI789", "owner_id": 3},
    {"brand": "Ford", "model_name": "F-150", "model_year": "2017", "color": "White", "registration_plate": "JKL012", "owner_id": 4},
    {"brand": "Audi", "model_name": "A4", "model_year": "2021", "color": "Silver", "registration_plate": "MNO345", "owner_id": 5},
    {"brand": "Mercedes", "model_name": "E-Class", "model_year": "2020", "color": "Gray", "registration_plate": "PQR678", "owner_id": 6},
    {"brand": "BMW", "model_name": "X5", "model_year": "2019", "color": "Black", "registration_plate": "STU901", "owner_id": 7},
    {"brand": "Kia", "model_name": "Optima", "model_year": "2016", "color": "White", "registration_plate": "VWX234", "owner_id": 8},
    {"brand": "Nissan", "model_name": "Altima", "model_year": "2018", "color": "Red", "registration_plate": "YZA567", "owner_id": 9},
    {"brand": "Hyundai", "model_name": "Sonata", "model_year": "2020", "color": "Blue", "registration_plate": "BCD890", "owner_id": 10},
    {"brand": "Toyota", "model_name": "Corolla", "model_year": "2015", "color": "Black", "registration_plate": "EFG123", "owner_id": 1},
    {"brand": "Honda", "model_name": "Civic", "model_year": "2019", "color": "Gray", "registration_plate": "HIJ456", "owner_id": 2},
    {"brand": "Ford", "model_name": "Mustang", "model_year": "2018", "color": "Red", "registration_plate": "KLM789", "owner_id": 3},
    {"brand": "Chevrolet", "model_name": "Cruze", "model_year": "2017", "color": "White", "registration_plate": "NOP012", "owner_id": 4},
    {"brand": "Audi", "model_name": "Q5", "model_year": "2020", "color": "Black", "registration_plate": "QRS345", "owner_id": 5},
    {"brand": "Mercedes", "model_name": "GLC", "model_year": "2019", "color": "Silver", "registration_plate": "TUV678", "owner_id": 6},
]

for car_data in cars_data:
    car = Car(**car_data)
    session.add(car)

session.commit()

session.close()
