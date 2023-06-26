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
    _fields = {
        'name',
        'email',
        'image',
        'last_active',
        'created_account'
        'assignments',
        'events'
    }

class Professor(Frame):
     _fields = {
        'name',
        'email',
        'image',
        'last_active',
        'created_account'
        'students',
        'assignments',
        'events'
     }

class Assignments(SubFrame):
    _fields = {
        'title',
        'assignment',
        'date_added',
        'due_date',
        'notes',
        'comments'
    }

class Comments(SubFrame):
    _fields = {
        'user_id',
        'comment_date',
        'comment'
    }

class Notes(SubFrame):
    _fields = {
        'title',
        'note',
        'date_added'
    }

class Events(SubFrame):
    _fields = {
        'title',
        'event',
        'event_date',
        'event_type'
    }



