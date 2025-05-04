from email.policy import HTTP
from fastapi import FastAPI, HTTPException
from market.models import ItemPayload

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "OK"}   


market_list: dict[int, ItemPayload] = {}

# Route to add a item
@app.post("/items/{item_name}/{quantity}")
def add_item(item_name: str, quantity: int):
    if quantity <= 0:
        raise HTTPException(status_code=400, detail="Quantity must be greater than 0.")
    # if item already exists, we'll just add the quantity.
    # get all item names
    items_ids = {item.item_name: item.item_id if item.item_id is not None else 0 for item in market_list.values()}
    if item_name in items_ids.keys():
        # get index of item_name in item_ids, which is the item_id
        item_id = items_ids[item_name]
        market_list[item_id].quantity += quantity
    # otherwise, create a new item
    else:
        # generate an ID for the item based on the highest ID in the grocery_list
        item_id = max(market_list.keys()) + 1 if market_list else 0
        market_list[item_id] = ItemPayload(
            item_id=item_id, item_name=item_name, quantity=quantity
        )

    return {"item": market_list[item_id]}
    
