import os

class Config:
    POPULAR_QUOTE = "http://quotes.stormconsultancy.co.uk/popular.json"
    NEW_QUOTE = "http://quotes.stormconsultancy.co.uk/quotes/1.json?callback=my_method"
    SECRET_KEY = os.environ.get('SECRET_KEY')
    
class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}