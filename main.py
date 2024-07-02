from typing import Union
from fastapi import FastAPI
import getpass
import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = getpass.getpass()
os.environ["OPENAI_API_KEY"] = ""


model = ChatOpenAI(model="gpt-3.5-turbo")

app = FastAPI()


@app.get("/")
def read_root():
    return {"version": "0.0.1"}


@app.get("/send")
def read_root(content: str = ""):
    response = model.invoke([HumanMessage(content=content)])
    return {"content": response.content}
