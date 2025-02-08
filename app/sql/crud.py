from sqlalchemy.orm import Session
from . import models, schemas
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_admin_by_name(db: Session, name: str):
    return db.query(models.Admin).filter(models.Admin.name == name).first()

def create_admin(db: Session, admin: schemas.AdminCreate):
    hashed_password = pwd_context.hash(admin.password)
    db_admin = models.Admin(name=admin.username, hashed_password=hashed_password)
    db.add(db_admin)
    db.commit()
    db.refresh(db_admin)
    return db_admin

def create_user(db: Session, guest: schemas.UserCreate):
  db_guest = models.Guest(**guest.dict())
  db.add(db_guest)
  db.commit()
  db.refresh(db_guest)
  return db_guest


def get_hotel(db: Session, hotel_id: int):
    return db.query(models.Hotel).filter(models.Hotel.id == hotel_id).first()

def get_hotels(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Hotel).offset(skip).limit(limit).all()

def create_hotel(db: Session, hotel: schemas.HotelCreate):
    db_hotel = models.Hotel(**hotel.dict())
    db.add(db_hotel)
    db.commit()
    db.refresh(db_hotel)
    return db_hotel

def get_user_by_username(db: Session, username: str):
  return db.query(models.User).filter(models.User.username == username).first()

def get_user_by_id(db: Session, id: int):
  return db.query(models.User).filter(models.User.id == id).first()


def get_guest(db: Session, guest_id: int):
    return db.query(models.Guest).filter(models.Guest.id == guest_id).first()

def get_guests(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Guest).offset(skip).limit(limit).all()

def create_guest(db: Session, guest: schemas.GuestCreate):
    db_guest = models.Guest(**guest.dict())
    db.add(db_guest)
    db.commit()
    db.refresh(db_guest)
    return db_guest


def create_posts(db: Session, posts: schemas.PostCreate):
  db_post = models.Post(**posts.dict())
  db.add(db_post)
  db.commit() 
  db.refresh(db_post)
  return db_post