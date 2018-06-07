class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI_FORMAT = 'mysql+pymysql://{user}:{pwd}@{host}:{port}/{db}'
    DATABASE_URI = 'sqlite://:memory:'



class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'


class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE_URI_FORMAT = 'mysql+pymysql://{user}:{pwd}@{host}:{port}/{db}'
    SQLALCHEMY_DATABASE_URI = DATABASE_URI_FORMAT.format(user='root',pwd='root',host='127.0.0.1',port='3306',db='crawl_manger')


class TestingConfig(Config):
    TESTING = True