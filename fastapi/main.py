from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import aiomysql
from models import Item, UpdateStatus


app = FastAPI()

items = []

@app.get('/')
async def root():
    return {"Hello" : "World"}

@app.post("/items")
async def create_item(item:Item):
    items.append(item)
    return {"Message" : "Updated"}

@app.get('/items', response_model=list[Item])
async def list_items(limit: int = 20):
    return items[0:limit]

@app.get("/items/{item_id}", response_model=Item)
async def get_item(item_id:int) -> Item:
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail="Item not found")
    
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    if item_id < len(items):
        items.pop(item_id)
        return {"message": "Todo has been deleted"}
    raise HTTPException(status_code=404, detail="Item not found")

@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id:int, status: UpdateStatus) -> Item:
    if item_id < len(items):
        items[item_id].is_done = status.is_done
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail="Item not found")