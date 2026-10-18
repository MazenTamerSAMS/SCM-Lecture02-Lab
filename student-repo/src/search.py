from src.inventory import PRODUCTS


def search_product(product_id):
    """Return a product name when the ID exists."""
    return PRODUCTS.get(product_id)
