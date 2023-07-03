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
        'events',
        'messages'
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
        'events',
        'messages'
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
        'comment',
        'replies'
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

class Messages(SubFrame):
    _fields = {
        'sender',
        'date_sent',
        'subject',
        'message'
    }

class Discussion(SubFrame):
       _fields = {
          'discussion_id',
          'topic',
          'media',
          'created_at',
          'comments'
       }

class Replies(SubFrame):
     _fields = {
          'user_id',
          'reply_date',
          'reply'
     }
