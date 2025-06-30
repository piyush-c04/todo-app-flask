from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
load_dotenv()
#create a SQLAlchemy instance
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    app.secret_key = os.environ.get("SECRET_KEY", "fallback-key")
    app.db_url = os.environ.get("DATABASE_URL", "sqlite:///todo.db")
    
    app.config['SQLALCHEMY_DATABASE_URI'] = app.db_url
    app.config['SECRET_KEY'] = app.secret_key
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False   

    #Link the SQLAlchemy instance to the Flask app
    db.init_app(app)
    
    from app.routes.auth import auth_bp
    from app.routes.tasks import tasks_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(tasks_bp)  
    
    return app
    

    