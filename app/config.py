import os

class Config:
    SECRET_KEY = '1c20a412ab0f6fef538768f3174b15e2'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://crabs:Greenland@localhost/pitches'
    
class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI =os.environ.get("DATABASE_URL")

class DevConfig(Config):
    DEBUG = True
    
config_options = {
'development':DevConfig,
'production':ProdConfig
}