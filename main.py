from database import thanksgiving_potluck

from fastapi import FastAPI, HTTPException
from database import thanksgiving_potluck
from typing import List, Optional

app = FastAPI(
    title="Tulane Thanksgiving Potluck API",
    description="A fun API for managing Tulane's campus Thanksgiving potluck contributions!",
    version="1.0.0"
)

print(thanksgiving_potluck)

# Root endpoint
@app.get("/")
async def root():
    return {
        "message": "Welcome to Tulane's Thanksgiving Potluck API! 🦃"
    }

# GET endpoint - Get all potluck items
@app.get("/potluck")
async def get_all_dishes():
    # Function will:
    # 1. Return all dishes in the potluck
    pass

# GET endpoint - Get a potluck item
@app.get("/potluck/{dish_id}")
async def get_dish(dish_id: int):
    # Function will:
    # 1. Find dish by ID in thanksgiving_potluck
    # 2. Return found dish
    pass

# POST endpoint - Add a new dish to the potluck
@app.post("/potluck")
async def add_dish():
    # Function will:
    # 1. Validate the incoming dish data
    # 2. Generate a new ID
    # 3. Add to thanksgiving_potluck database
    pass

# PATCH endpoint - Update dish details
@app.patch("/potluck/{dish_id}")
async def update_dish(dish_id: int):
    # Function will:
    # 1. Find dish by ID in thanksgiving_potluck
    # 2. Update only the provided fields
    # 3. Return updated dish
    pass

# DELETE endpoint - Remove a dish from the potluck
@app.delete("/potluck/{dish_id}")
async def delete_dish(dish_id: int):
    # Function will:
    # 1. Find and remove dish from thanksgiving_potluck
    # 2. Return success message
    pass
