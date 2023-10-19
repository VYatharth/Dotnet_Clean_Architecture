from pydantic import BaseModel
from datetime import datetime
from typing import List


class UserRequestSchema(BaseModel):
  username: str
  email: str
  password: str

class UserResponseSchema(BaseModel):
  username: str
  email: str
  class Config():
    from_attributes = True




# For PostDisplay
class User(BaseModel):
  username: str
  class Config():
    from_attributes = True


class UserAuth(BaseModel):
  id: int
  username: str
  email: str