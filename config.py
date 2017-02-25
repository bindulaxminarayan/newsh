import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


baseDir = os.path.dirname(os.path.abspath(__file__))

appName = "Newsh"
dbName = "Newsh.db"
dbFilename = os.path.join(baseDir, dbName)


""" Create application instances """
app = Flask(appName)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///%s' % (dbFilename)
db = SQLAlchemy(app)
