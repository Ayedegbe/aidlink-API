from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

app = FastAPI(title="AidLink API", version="1.0.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow everything (you can restrict this later)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# if os.path.exists("frontend"):
#     app.mount("/frontend", StaticFiles(directory="frontend", html=True), name="frontend")

# In-memory data
supplies = []
locations = []
requests = []
supply_id = 1
location_id = 1
request_id = 1

# Models
class Supply(BaseModel):
    name: str
    quantity: int
    unit: str = "units"

class SupplyOut(Supply):
    id: int

class Location(BaseModel):
    name: str
    region: str

class LocationOut(Location):
    id: int

class Request(BaseModel):
    locationId: int
    supplyName: str
    quantity: int

class RequestOut(Request):
    id: int

# Endpoints

@app.get("/supplies", response_model=List[SupplyOut])
def get_supplies():
    return supplies

@app.post("/supplies", response_model=SupplyOut, status_code=201)
def add_supply(supply: Supply):
    global supply_id
    new_supply = {**supply.dict(), "id": supply_id}
    supplies.append(new_supply)
    supply_id += 1
    return new_supply

@app.get("/locations", response_model=List[LocationOut])
def get_locations():
    return locations

@app.post("/locations", response_model=LocationOut, status_code=201)
def add_location(location: Location):
    global location_id
    new_location = {**location.dict(), "id": location_id}
    locations.append(new_location)
    location_id += 1
    return new_location

@app.post("/requests", response_model=RequestOut, status_code=201)
def create_request(req: Request):
    global request_id
    if not any(loc["id"] == req.locationId for loc in locations):
        raise HTTPException(status_code=404, detail="Location not found")
    new_request = {**req.dict(), "id": request_id}
    requests.append(new_request)
    request_id += 1
    return new_request

@app.get("/")
def read_index():
    return FileResponse(os.path.join("frontend", "index.html"))
