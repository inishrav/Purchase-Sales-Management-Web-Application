# config.py
class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'  # here we can given any name for database because it is just storing the data
    SQLALCHEMY_TRACK_MODIFICATIONS = False
