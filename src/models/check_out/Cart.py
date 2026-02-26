from src.models.check_out import Product
class Cart:

    def __init__(self):
        self.products = []

    def add_product_to_cart(self, product: Product):
        self.products.append(product)

    def remove_product_from_cart(self, product: Product):
        found_item = self.find_from_cart_by_name(product)
        if found_item:
            self.products.remove(found_item)
            return f"Item {found_item.name} removed from cart"
        raise ValueError(f"Product {product.name} not in cart")

    def find_from_cart_by_name(self, product: Product):
        for item in self.products:
            if item.name == product.name:
                return item
        return None