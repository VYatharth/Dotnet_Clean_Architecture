from fastapi import FastAPI
from models.BaseModel import init
from routers.UserRouter import UserRouter
from sqlalchemy.sql.functions import user
from metadata.Tags import Tags
from fastapi.middleware.cors import CORSMiddleware
from configs.Environment import get_environment_variables

# Application Environment Configuration
env = get_environment_variables()

# Core Application Instance
app = FastAPI(
    title=env['APP_NAME'],
    openapi_tags=Tags,
)


app.include_router(UserRouter)

origins = [
  'http://localhost:3000',
  'http://localhost:3001',
  'http://localhost:3002'
]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=['*'],
  allow_headers=['*']
)


# Initialise Data Model Attributes
init()