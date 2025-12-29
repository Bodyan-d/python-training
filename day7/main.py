from fastapi import FastAPI, HTTPException
import uuid
from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    price: float
    in_stock: bool

app = FastAPI()
products = []

@app.get("/")
def root():
    return {"message": "Hello, FastAPI"}

@app.get("/health")
def ping():
    return {"status": "ok"}

@app.post("/products", status_code=201)
def create_product(product: ProductCreate):
    new_product = {
        "id": str(uuid.uuid4()),
        "name": product.name,
        "price": product.price,
        "in_stock": product.in_stock
    }
    products.append(new_product)
    return new_product

@app.get("/products")
def get_all_products():
    return products

@app.get("/products/{product_id}")
def get_product(product_id: str):
    for product in products:
        if product["id"] == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")

@app.put("/products/{product_id}")
def update_product(product_id: str, product: ProductCreate):
    for p in products:
        if p["id"] == product_id:
            p["name"] = product.name
            p["price"] = product.price
            p["in_stock"] = product.in_stock
            return p
    raise HTTPException(status_code=404, detail="Product not found")

@app.delete("/products/{product_id}", status_code=204)
def delete_product(product_id: str):
    for p in products:
        if p["id"] == product_id:
            products.remove(p)
            return
    raise HTTPException(status_code=404, detail="Product not found")