from fastapi import FastAPI
from bucket import Bucket

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to token rate limiter project"}


@app.post("/buckets/")
def create_bucket(size):
    bucket = Bucket(size)
    return {"id": bucket.id}


@app.post("/buckets/{bucket_id}/remove-token")
def remove_token():
    # need to get a bucket
    return {"message": "No database to get bucket from"}
