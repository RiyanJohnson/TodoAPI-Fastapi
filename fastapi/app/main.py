from fastapi import FastAPI, HTTPException
from app.database import database, metadata, engine
from app.models import items_table
from app.schemas import Item, ItemIn

import sqlalchemy

metadata.create_all(bind=engine)

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or restrict to ["http://127.0.0.1:5500"] if using Live Server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get('/')
async def root():
    return {"Hello" : "World"}

@app.post("/items")
async def create_item(item:ItemIn):
    query = items_table.insert().values(**item.dict()) # ** used to unpack the dict
    last_id = await database.execute(query)
    return {"Message" : "Updated"}

@app.get('/items', response_model=list[Item])
async def list_items(limit: int = 20):
    query = items_table.select().where(items_table.c.id > 1)
    return await database.fetch_all(query)

@app.get("/items/{item_id}", response_model=Item)
async def get_item(item_id:int) -> Item:
    query = items_table.select().where(items_table.c.id == item_id)
    result = await database.fetch_one(query)
    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail="Item not found")
    
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    query = items_table.delete().where(items_table.c.id == item_id)
    await database.execute(query)
    return {"message" : "Item has been deleted"}

@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, update: ItemIn):
    query = items_table.update().where(items_table.c.id == item_id).values(**update.dict())
    await database.execute(query)
    return {**update.dict(), "id": item_id}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
