from fastapi import FastAPI

app= FastAPI()

@app.get("/")
def get_id():
    return {"message":"this is your id"}

