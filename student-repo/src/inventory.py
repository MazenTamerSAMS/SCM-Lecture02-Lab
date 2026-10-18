PRODUCTS = {
    "P001": "Laptop",
    "P002": "Monitor",
    "P003": "Keyboard",
}

STOCK = {
    "P001": 10,
    "P002": 7,
    "P003": 25,
}


def list_products():
    return list(PRODUCTS.items())


def stock_is_valid(quantity):
    return quantity >= 0


def format_product(product_id):
    name = PRODUCTS.get(product_id)
    return f"{product_id}: {name}" if name else "Unknown product"


def check_stock(product_id):
    return STOCK.get(product_id)
