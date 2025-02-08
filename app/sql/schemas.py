from typing import Optional
from pydantic import BaseModel, EmailStr


# Hotel Schema
class HotelBase(BaseModel):
    name: str
    address: str
    phone: str
    budget: str
    monthly_expenses: str

class HotelCreate(HotelBase):
    pass

class Hotel(HotelBase):
  id: int

  class Config:
      orm_mode = True

# User Schema
class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True

# Admin Schema
class AdminBase(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None

class AdminCreate(AdminBase):
    password: str

class Admin(AdminBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True

# Room Schema
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

# Guest Schema

class GuestBase(BaseModel):
    name: str
    email: EmailStr
    phone: str

class GuestCreate(GuestBase):
  pass

class Guest(GuestBase):
  id: int

  class Config:
      orm_mode = True

# Booking Schema
class BookingBase(BaseModel):
    user_id: int
    room_id: int
    start_date: str
    end_date: str

class BookingCreate(BookingBase):
    pass

class Booking(BookingBase):
    id: int

    class Config:
        orm_mode = True


# Posts Schema

class PostBase(BaseModel):
    title: str
    content: str
    author: str

class PostCreate(PostBase):
    pass

class Post(PostBase):
  id: int
  class Config:
    orm_mode = True