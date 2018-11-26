from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()


class Config(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/db"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = False


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)


class Default(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return "Default: %d" % self.id


if __name__ == '__main__':
    app.run()




