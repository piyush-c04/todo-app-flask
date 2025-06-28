from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

#create a SQLAlchemy instance
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
    app.config['SECRET_KEY'] = 'your_secret_key_here'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False   

    #Link the SQLAlchemy instance to the Flask app
    db.init_app(app)
    
    from app.routes.auth import auth_bp
    from app.routes.tasks import tasks_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(tasks_bp)  
    
    return app
    

    