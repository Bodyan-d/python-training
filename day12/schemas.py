from pydantic import BaseModel, Field
from typing import Optional
import uuid

class ProductCreate(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    price: float = Field(gt=0)
    in_stock: bool
    
    
class ProductUpdate(BaseModel):
    name: Optional[str] = Field(default=None, min_length=2, max_length=50)
    price: Optional[float] = Field(default=None, gt=0)
    in_stock: Optional[bool] = None
    
class ProductResponse(ProductCreate):
    id: str = Field(str(uuid.uuid4()))