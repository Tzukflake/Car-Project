Car Management API

This project is a Flask-based API designed to manage cars and users. The system provides CRUD functionality (Create, Read, Update, Delete) for both cars and users using SQLAlchemy as the ORM and SQLite as the database. The API allows clients to perform operations like retrieving information about cars and users, adding new records, and updating or deleting existing ones.

Features
- Car Management:
- Create, update, delete, and retrieve information about cars.
- Cars are linked to owners (users), and detailed information about the car and owner can be retrieved.
- User Management:
- Create, update, delete, and retrieve information about users.
- Users can be linked to one or more cars.

  
Technologies Used
- Python 3.x
- Flask: Microframework for building web applications.
- Flask-SQLAlchemy: Extension for Flask that adds support for SQLAlchemy.
- SQLite: Lightweight database used for local storage.
- SQLAlchemy: ORM (Object Relational Mapping) to handle database interactions.
