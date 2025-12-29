from fastapi import FastAPI, HTTPException
from schemas import ProductResponse, ProductCreate, ProductUpdate
import logging
import uuid

app = FastAPI()

products = []

@app.post("/products", status_code=201, response_model=ProductResponse)
def add_product(product: ProductCreate):
    new_product = {
        "id": str(uuid.uuid4()),
        "name": product.name,
        "price": product.price,
        "in_stock": product.in_stock
    }
    products.append(new_product)
    return new_product

@app.get("/products", status_code=200, response_model=list[ProductResponse])
def get_all_products():
    return products

@app.get("/products/{id}", status_code=200, response_model=ProductResponse)
def get_one_products(id: str):
    product = next((p for p in products if p["id"] == id), None)

    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    return product

@app.patch("/products/{id}")
def update_product(id, new_product: ProductUpdate):
    product = next((p for p in products if p["id"] == id), None)
    
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    logging.info(new_product)
    if new_product.name is not None:
        product["name"] = new_product.name
    if new_product.price is not None:
        product["price"] = new_product.price
    if new_product.in_stock is not None:
        product["in_stock"] = new_product.in_stock

    return product


        