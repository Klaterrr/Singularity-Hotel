from pydantic import BaseModel
from typing import List, Optional
from datetime import date


class AdminCreate(BaseModel):
  username: str
  password: str

class HotelBase(BaseModel):
  name: str
  address: str
  phone: str
  total_budget: int
  monthly_expenses: int


class HotelCreate(HotelBase):
  pass


class Hotel(HotelBase):
  id: int

  class Config:
    orm_mode = True


class RoomBase(BaseModel):
  hotel_id: int
  room_number: int
  type: str
  price: float


class RoomCreate(RoomBase):
  pass


class Room(RoomBase):
  id: int

  class Config:
    orm_mode = True


class User(BaseModel):
  username: str
  password: str
  role: str

class UserCreate(User):
  pass

class TokenData(BaseModel):
  username: Optional[str] = None

# Similar classes would be created for Guest, Staff, Administrator, Reservation, Payment, and Inventory


class GuestBase(BaseModel):
  first_name: str
  last_name: str
  email: str
  phone: str


class GuestCreate(GuestBase):
  pass


class Guest(GuestBase):
  id: int

  class Config:
    orm_mode = True
