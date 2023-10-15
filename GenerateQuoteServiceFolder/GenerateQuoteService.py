from fastapi import FastAPI
from quote import quote

app = FastAPI()

@app.get("/quotes")
async def createQuote():
    quote_of_the_day = quote('family',limit=1)
    return quote_of_the_day