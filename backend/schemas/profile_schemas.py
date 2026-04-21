from pydantic import BaseModel

class ProfileCreate(BaseModel):
    stream:str
    class_level:str
    language:str
    