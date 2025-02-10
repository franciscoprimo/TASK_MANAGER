import os
SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///taskmanager.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  
