from flask import Flask
from mongokit import Connection

app = Flask(__name__)
app.debug = True

db = Connection()
from models.user import User

from app.controllers import *