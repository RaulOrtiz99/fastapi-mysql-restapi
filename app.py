from fastapi import FastAPI 

app= FastAPI()


@app.get('/')
def hellowordl():
    return "Hello world"