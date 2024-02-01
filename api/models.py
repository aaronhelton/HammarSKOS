from pydantic import BaseModel

class Vocabulary(BaseModel):
    name: str
    description: str | None = None
    short_name: str
    local_path: str
    base_uri: str 
