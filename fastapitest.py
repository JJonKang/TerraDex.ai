from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
#https://youtu.be/iWS9ogMPOI0?si=olBjvhUW7200QW_w tutorial
#https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status for error codes

#with extension basemodel, curl has to change like this:
#curl.exe -X POST -H "Content-Type: application/json" -d '{"text":"apple"}' 'http://127.0.0.1:8000/items'
class Item(BaseModel):
    text: str = None
    is_done: bool = False

items = []

#start up server: python -m uvicorn main:app --reload

#get/post introduction testing 
@app.get("/")
def root():
    return {"Hello": "World"}

#curl.exe -X POST -H "Content-Type: application/json" 'http://127.0.0.1:8000/items?item=apple'
#change to this one instead- curl.exe -X POST -H "Content-Type: application/json" -d '{"text":"apple"}' 'http://127.0.0.1:8000/items'
#use that for adding items i guess...
@app.post("/items")
def create_item(item: Item):
    items.append(item)
    return item

#curl.exe -X GET 'http://127.0.0.1:8000/items?limit=3'
#get first three items
#default is 10
@app.get("/items", response_model=list[Item])
def list_items(limit: int = 10):
    return items[0:limit]

#curl.exe -X GET http://127.0.0.1:8000/items/0
#use that for getting items via index at the end
@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int) -> Item:
    if item_id < len(items):
        return items[item_id]
    raise HTTPException(status_code=404, detail=f"Item {item_id} not found") # accounts for errors for out of bounds items list



#note that if main.py is refreshed, items list will be reset
#interactive documentation is here: #http://127.0.0.1:8000/docs#/ OR http://127.0.0.1:8000/redoc