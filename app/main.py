# from flask import Flask, request, abort
from redis import Redis
from fastapi import FastAPI

app = FastAPI()
redis = Redis(host='172.17.0.1', port=6379)

#import test_routes


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


#if __name__ == '__main__':
  #  app.run(host='0.0.0.0')
