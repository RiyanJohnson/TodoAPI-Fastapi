from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    text: str = None
    is_done: bool = False
    description: str = None
class UpdateStatus(BaseModel):
    is_done: bool
