from pydantic import BaseModel, Field, EmailStr

class HotelSchema(BaseModel):
  id : int = Field(default = None)
  name : str = Field(default = None)
  address : str = Field(default = None)
  phone : str = Field(default = None)
  budget : str = Field(default = None)
  class Config():
    schema_demo = {
      "post_demo": {
        "id" : "Post Title",
        "name" : "Hotel Name",
        "address" : "Post Content",
        "phone" : "Post author",
        "Budget" : "Start budget"
      }
    }


class PostSchema(BaseModel):
  id : int = Field(default = None)
  title : int = Field(default = None)
  content : int = Field(default = None)
  class Config():
    schema_demo = {
      "post_demo": {
        "title" : "Post Title",
        "content" : "Post Content",
        "author" : "Post author"
      }
    }

class UserSchema(BaseModel):
  fullname: str = Field(...)
  email: EmailStr = Field(...)
  password: str = Field(...)

  class Config:
      schema_extra = {
          "example": {
              "fullname": "Yulia Komarova",
              "email": "uejkao@goa.com",
              "password": "any"
          }
      }

class UserLoginSchema(BaseModel):
  email: EmailStr = Field(...)
  password: str = Field(...)

  class Config:
      schema_extra = {
          "example": {
              "email": "uejkao@goa.com",
              "password": "any"
          }
      }