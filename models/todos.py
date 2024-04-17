from pydantic import BaseModel

class Todo(BaseModel):
    name: str
    description: str
    complete: bool
    
class Product(BaseModel):
    name: str
    price: float
    quantity: int
    description: str
    
class Category(BaseModel):
    pass