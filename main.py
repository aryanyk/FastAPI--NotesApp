from typing import Union

from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates



app = FastAPI()

@app.get("/")
def index():
  return {"date":{"Name":"Aryan Khandhadiya"}}





