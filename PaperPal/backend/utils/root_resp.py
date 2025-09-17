# python imports
from pydantic import BaseModel

# root endpoint - Response model
class RootResponseModel(BaseModel):
    response: str
