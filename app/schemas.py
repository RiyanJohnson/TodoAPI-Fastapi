from pydantic import BaseModel

class ItemIn(BaseModel):
    text: str
    is_done: bool = False
    description: str = None

class Item(ItemIn):
    id: int
