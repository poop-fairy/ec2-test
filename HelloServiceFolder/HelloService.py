from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return{"message":"What's Good Human"}
    