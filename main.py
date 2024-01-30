from fastapi import FastAPI

# create an app instance of FastAPI
app = FastAPI()

# create a route for the root endpoint

@app.get("/")
def index():
    return "hello world!"

@app.get("/blogs")
def index2():
    return "All the blogs"

@app.get("/point")
def index2():
    return "point"