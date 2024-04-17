def individual_serial(todo) -> dict:
    
    return {
        "id": str(todo["_id"]),
        "name": todo["name"],
        "description": todo["description"],
        "complete": todo["complete"]
    }
    
def list_serial(todos) -> list:
    return [individual_serial(todo) for todo in todos]


def product_serial(product) -> dict:
    return {
        "id" : str(product["_id"]),
        "name": product["name"],
        "price": product["price"],
        "quantity": product["quantity"],
        "description": product["description"]
    }

def list_product(products) -> list:
    return [product_serial(product) for product in products]