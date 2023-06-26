from pymongo import MongoClient
from mongoframes import *
from dotenv import load_dotenv
from datetime import datetime
from passlib.hash import pbkdf2_sha256
import os
import uuid

load_dotenv('.env')
Frame._client = MongoClient(os.getenv('MONGO_URI'))

class Student(Frame):
    pass

class Professor(Frame):
    pass

class Assignments(SubFrame):
    pass

class Events(SubFrame):
    pass



