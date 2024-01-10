# from flask import Flask, request, abort
from redis import Redis
from fastapi import FastAPI
from router import test_routes

app = FastAPI()
redis = Redis(host='172.17.0.1', port=6379)

app.include_router(test_routes.router)


@app.get('/')
def hello():
    return 'Hello, World!'

@app.get('/write')
def writeRedis(q):
    redis.set('user-input', q)
    return q

@app.get('/read')
def readRedis():
    return redis.get('user-input')