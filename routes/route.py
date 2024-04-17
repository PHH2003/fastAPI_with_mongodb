from fastapi import APIRouter
from models.todos import Product, Todo
from config.database import collection_name, collection_product
from schema.schemas import list_product, list_serial, product_serial
from bson import ObjectId

router = APIRouter()

#GET Request Method
@router.get("/")
async def get_todos():
    todos = list_serial(collection_name.find())
    return todos

# POST Request Method
@router.post("/")
async def post_todos(todo: Todo):
    collection_name.insert_one(dict(todo))

#PUT Request Method
@router.put("/{id}")
async def put_todos(id:str, todo:Todo):
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(todo)})

#Delete Request Method
@router.delete("/{is}")
async def delete_todos(id: str, todo: Todo):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})
    
@router.post("/product/create")
async def create_product(product: Product):
    collection_product.insert_one(dict(product))

@router.get("/product")
async def get_all_product():
    products = list_product(collection_product.find())
    return products 

@router.get("/product/{id_product}")
async def get_one_product(id_product: str):
    found_product =collection_product.find_one({"_id": ObjectId(id_product)})
    return product_serial(found_product)

@router.put("/product/{id_product}")
async def update_product(id_product: str, product: Product):
    collection_product.find_one_and_update({"_id": ObjectId(id_product)}, {"$set": dict(product)})

@router.delete("/product/{id_product}")
async def delete_product(id_product: str, product: Product):
    collection_product.find_one_and_delete({"_id": ObjectId(id_product)})  