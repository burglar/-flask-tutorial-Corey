import os



class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    #SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://flaskblog_user:flaskblog_user@localhost:3306/flaskblog_db'
    #SQLALCHEMY_DATABASE_URI = 'postgres://fblog:fblog@127.0.0.1/fb'
    #SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://fblog:fblog@127.0.0.1/fb'
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    ########################################################### 
    # Test email funcionality:
    # python -m smtpd -n -c DebuggingServer localhost:8025
    ########################################################### 
    #MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    #MAIL_PORT = 587
    MAIL_PORT = os.environ.get('MAIL_PORT')
    #MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')