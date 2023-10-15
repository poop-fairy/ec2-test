import sys
sys.path.append("./HelloServiceFolder")
sys.path.append("./GenerateQuoteServiceFolder")

from fastapi import FastAPI
from GenerateQuoteService import app as quote_app_router
from HelloService import app as hello_app_router

app = FastAPI()
app.mount("/helloservice",hello_app_router)
app.mount("/quoteservice",quote_app_router)