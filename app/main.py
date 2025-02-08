import uvicorn
from fastapi import FastAPI, Body

from app.auth.handler import signJWT
from app.models import PostSchema, UserSchema, UserLoginSchema


def check_user(data: UserLoginSchema):
  for user in users:
    if user.email == data.email and user.password == data.password:
      return True
  return False



posts = [
  {
    'id': 1,
    'title': 'Post 1',
    'content': 'First post content',
  },
  {
    'id': 2,
    'title': 'Post 2',
    'content': 'Second post content',
  },
  {
    'id': 3,
    'title': 'Post 3',
    'content': 'Third post content',
  }
]

users = []


app = FastAPI()

@app.get("/", tags = ['test'])
def greet():
  return {"hello":"world"}


# Posts
@app.get("/posts", tags = ['posts'])
def get_posts():
  return {'data':posts}

@app.get("/posts/{id}", tags = ['posts'])
def get_one_post(id: int):
  if id > len(posts) or id < 1:
    return {
      "error":"Post with that ID does not exist"
    }
  for post in posts:
    if post['id'] == id:
      return {'data':post}

@app.post("/posts", tags = ['posts'])
def add_post(post: PostSchema):
  post.id = len(posts) + 1
  posts.append(post.dict())
  return {'info':'Post Added!'}

@app.post("/user/signup", tags=["user"])
def create_user(user: UserSchema = Body(...)):
    users.append(user) # replace with db call, making sure to hash the password first
    return signJWT(user.email)


@app.post("/user/login", tags=["user"])
def user_login(user: UserLoginSchema = Body(...)):
    if check_user(user):
        return signJWT(user.email)
    return {
        "error": "Wrong login details!"
    }

"""
from fastapi import FastAPI, Depends, HTTPException, status, APIRouter, Form
from sqlalchemy.orm import Session
from typing import List, Annotated
from fastapi.security import HTTPBasic, HTTPBasicCredentials, OAuth2PasswordBearer
from passlib.context import CryptContext

# Import your models and database settings
from Singularity_Hotel import models, schemas, crud
from Singularity_Hotel.database import SessionLocal, engine

app = FastAPI()

security = HTTPBasic()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Dependency
def get_db():
  db = SessionLocal()
  try:
      yield db
  finally:
      db.close()
    
users = {
    "testuser": {
        "username": "testuser",
        "hashed_password": pwd_context.hash("testpassword"),
    }
}
def authenticate_user(username: str, password: str):
  user = users.get(username)
  if not user:
      return False
  if not pwd_context.verify(password, user["hashed_password"]):
      return False
  return user

@app.post("/login")
def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
  return {"username": username}
"""
"""
def login(credentials: HTTPBasicCredentials = Depends(security)):
  user = authenticate_user(credentials.username, credentials.password)
  if not user:
      raise HTTPException(
          status_code=status.HTTP_401_UNAUTHORIZED,
          detail="Incorrect username or password",
          headers={"WWW-Authenticate": "Basic"},
      )
  return {"Welcome": user["username"]}
"""
"""
@app.post("/token", response_model=schemas.Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
  user = crud.get_user_by_username(db, username=form_data.username)
  if not user or not verify_password(form_data.password, user.hashed_password):
      raise HTTPException(
          status_code=status.HTTP_401_UNAUTHORIZED,
          detail="Incorrect username or password",
          headers={"WWW-Authenticate": "Bearer"},
      )
  access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
  access_token = create_access_token(
      data={"sub": user.username}, expires_delta=access_token_expires
  )
  return {"access_token": access_token, "token_type": "bearer"}
"""
"""
@app.get("/users/{username}", response_model=schemas.User)
def read_user(username: str, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=username)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/admin/add")
def add_new_admin(admin: schemas.AdminCreate, db: Session = Depends(get_db)):
    db_admin = crud.get_admin_by_name(db, name=admin.name)
    if db_admin:
        raise HTTPException(status_code=400, detail="Admin already registered")
    return crud.create_admin(db=db, admin=admin)

"""
"""
@app.get("/admin_menu")
def read_admin_menu(token: str = Depends(oauth2_scheme)):
    # Replace with your actual logic for admin menu
    ...

@app.get("/hotel/{hotel_id}", response_model=schemas.Hotel)
def read_hotel(hotel_id: int, db: Session = Depends(get_db)):
    db_hotel = crud.get_hotel(db, hotel_id=hotel_id)
    if db_hotel is None:
        raise HTTPException(status_code=404, detail="Hotel not found")
    return db_hotel

@app.get("/finance/{hotel_id}", response_model=schemas.Finance)
def read_finance(hotel_id: int, db: Session = Depends(get_db)):
    db_finance = crud.get_finance(db, hotel_id=hotel_id)
    if db_finance is None:
        raise HTTPException(status_code=404, detail="Finance data not found")
    return db_finance
"""