from fastapi import FastAPI
from redis import Redis, RedisError
import socket

redis = Redis(host='redis', db=0, socket_connect_timeout=2, socket_timeout=2)
app = FastAPI()


@app.get("/")
def hello():
    try:
        visites = redis.incr("compteur")
    except RedisError:
        visites = "erreur de connection Redis, compteur desactive"
    return {"nb visites": visites}
