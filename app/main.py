from fastapi import FastAPI
from app.models.BaseModel import init
from app.routers.UserRouter import UserRouter
from app.metadata.Tags import Tags
from app.configs.Environment import get_environment_variables

# Application Environment Configuration
env = get_environment_variables()

# Core Application Instance
app = FastAPI(
    title=env['APP_NAME'],
    openapi_tags=Tags,
)

@app.get("/")
def index():
    return  'navigate to /docs route for open API spec'

app.include_router(UserRouter)

# Initialise Data Model Attributes
init()