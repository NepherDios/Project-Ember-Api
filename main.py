from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import routers
from routers import (
    ability_router,
    accessory_router,
    armor_router,
    armory_enchantment_router,
    equipment_common_attr_router,
    general_item_router,
    inventory_router,
    item_router,
    player_router,
    progress_router,
    quest_progress_router,
    quest_router,
    roll_stat_router,
    weapon_router,
)

# Initialize app
app = FastAPI(title="Project Ember", version="1.0.0")

# Include routers
app.include_router(ability_router.router)
app.include_router(accessory_router.router)
app.include_router(armor_router.router)
app.include_router(armory_enchantment_router.router)
app.include_router(equipment_common_attr_router.router)
app.include_router(general_item_router.router)
app.include_router(inventory_router.router)
app.include_router(item_router.router)
app.include_router(player_router.router)
app.include_router(progress_router.router)
app.include_router(quest_progress_router.router)
app.include_router(quest_router.router)
app.include_router(roll_stat_router.router)
app.include_router(weapon_router.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # replace "*" with your Unity app origin in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root endpoint
@app.get("/")
def root():
    return {"message": "Welcome to Project Ember RPG!"}
