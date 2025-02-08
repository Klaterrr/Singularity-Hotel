import uvicorn
from sqlalchemy.orm import Session
from fastapi import FastAPI, Body, Depends, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


import app.sql.models as models
import app.sql.schemas as schemas
from app.auth.bearer import JWTBearer
from app.auth.handler import signJWT
from app.models import PostSchema, UserSchema, UserLoginSchema
from app.sql.crud import create_user, get_user_by_id
from app.sql.database import Base, SessionLocal, engine

Base.metadata.create_all(engine)

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()



def check_user(data: UserLoginSchema):
  for user in users:
    if user.email == data.email and user.password == data.password:
      return True
  return False


def get_current_user(db: Session = Depends(get_db)):
# This function should return the current user based on the request.
# You might fetch the user ID from the request's headers, cookies, etc.
# Then, fetch the user from the database and return it.
# For now, let's assume we have a function `get_user_id_from_request` that does this.
  user_id = get_user_by_id()
  user = db.query(models.User).filter(models.User.id == user_id).first()
  if user is None:
    raise HTTPException(status_code=404, detail="User not found")
  return user


def is_admin(user: schemas.User = Depends(get_current_user)):
  if user.role != "admin":
    raise HTTPException(status_code=403, detail="Operation not permitted")
  return True
  




app = FastAPI()
templates = Jinja2Templates(directory="templates")



@app.post(
  "/create/hotel/", response_model=schemas.User
)
def new_hotel(hotel_id: int, hotel: schemas.HotelCreate, db: Session = Depends(get_db)):
  hotel_id = models.Hotel(**hotel.dict())
  db.add(hotel_id)
  db.commit()
  db.refresh(hotel_id)
  return hotel_id

@app.get(
  "/hotel/{hotel_id}", response_model=schemas.User
)
def show_hotel(hotel_id: int, hotel: schemas.HotelCreate, db: Session = Depends(get_db)):
  hotel_id = models.Hotel(**hotel.dict())
  db_hotel = db.query(models.User).filter(models.Hotel.id == db_hotel).first()
  if db_hotel is None:
    raise HTTPException(status_code=404, detail="User not found")
  return templates.TemplateResponse("user.html", {"request": request, "user": db_hotel})

@app.post(
  "/create/room/", response_model=schemas.User
)
def new_room(room_id: int, room: schemas.RoomCreate, db: Session = Depends(get_db)):
  room_id = models.Room(**room.dict())
  db.add(room_id)
  db.commit()
  db.refresh(room_id)
  return room_id




@app.get("/users/", response_model=schemas.User)
def show_user(user: schemas.User, db: Session = Depends(get_db)):
  db_user = models.User(**user.dict())
  db.add(db_user)
  db.commit()
  db.refresh(db_user)
  return templates.TemplateResponse("user.html", {"request": request, "user": db_user})


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
  db_user = db.query(models.User).filter(models.User.id == user_id).first()
  if db_user is None:
    raise HTTPException(status_code=404, detail="User not found")
  return templates.TemplateResponse("user.html", {"request": request, "user": db_user})

@app.post(
  "/create/user/", response_model=schemas.User
)
def new_user(user_id: int, user: schemas.UserCreate, db: Session = Depends(get_db)):
  db_user = models.User(**user.dict())
  db.add(db_user)
  db.commit()
  db.refresh(db_user)
  return db_user

@app.put(
  "/users/{user_id}", response_model=schemas.User, 
  dependencies=[Depends(is_admin)]
)
def update_user(user_id: int, user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    for key, value in user.dict().items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.delete(
  "/users/{user_id}", response_model=schemas.User, 
  dependencies=[Depends(is_admin)]
)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_user)
    db.commit()
    return {"detail": "User deleted"}



@app.get("/", tags=['test'])
def greet():
  return {"hello": "world"}


# Posts
@app.get("/posts", tags=['posts'])
def get_posts(post_id: int, db: Session = Depends(get_db)):

  db_post = models.Post(**post.dict())
  db.add(db_post)
  db.commit()
  db.refresh(db_post)

  return {'data': db_post}


@app.get("/posts/{post_id}", tags=['posts'])
def get_one_post(post_id: int, db: Session = Depends(get_db)):

  db_post = db.query(models.Post).filter(models.Post.id == post_id).first()
  if db_post is None:
      raise HTTPException(status_code=404, detail="Post not found")
  return db_post


@app.post(
  "/create/post", tags=['posts'], 
  dependencies=[Depends(is_admin)]
)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db)):
  db_post = models.Post(**post.dict())
  db.add(db_post)
  db.commit()
  db.refresh(db_post)
  return db_post


@app.post("/user/signup", tags=["user"])
def signup_user(user: UserSchema = Body(...)):
  users.append(
      user)  # replace with db call, making sure to hash the password first
  return signJWT(user.email)


@app.post("/user/login", tags=["user"])
def user_login(user: UserLoginSchema = Body(...)):
  if check_user(user):
    return signJWT(user.email)
  return {"error": "Wrong login details!"}


"""
@app.get("/home/", response_class=schemas.User)
def home(user: schemas.User = Depends(get_current_user)):
  db_user = db.query(models.User).filter(models.User.id == user.id).first()
  if db_user is None:
    return user_login()
  return db_user
"""