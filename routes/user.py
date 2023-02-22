from fastapi import APIRouter 
from config.db import conn


user = APIRouter()

@user.get('/users')
def helloworld():
    return "hola mundo "

@user.get('/users')
def helloworld():
    return "hola mundo "

@user.get('/users')
def helloworld():
    return "hola mundo "

@user.get('/users')
def helloworld():
    return "hola mundo "



