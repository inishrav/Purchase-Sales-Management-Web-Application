'''import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your_secret_key'
'''
import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'  # Using SQLite
    SQLALCHEMY_TRACK_MODIFICATIONS = False
