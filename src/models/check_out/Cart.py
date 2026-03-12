from src.models.check_out.Product import Product

class Cart:
    def __init__(self):
        self.products = []

    def add_product_to_cart(self, product: Product):
        existing = self.find_from_cart_by_name(product)
        if existing:
            existing.set_quantity(existing.get_quantity() + product.get_quantity())
        else:
            self.products.append(product)

    def remove_product_from_cart(self, product: Product):
        found_item = self.find_from_cart_by_name(product)
        if found_item:
            self.products.remove(found_item)
            return f"Item {found_item.name} removed from cart"
        raise ValueError(f"Product {product.name} not in cart")

    def find_from_cart_by_name(self, product: Product):
        for item in self.products:
            if item == product:
                return item
        return None

    def get_total_items(self):
        return sum(product.quantity for product in self.products)

    def get_total_value(self):
        return sum(product.get_total_value() for product in self.products)

    def is_empty(self):
        return len(self.products) == 0

    def clear_cart(self):
        self.products.clear()

    def __str__(self):
        if self.is_empty():
            return "Cart is empty"
        cart_str = f"Cart ({self.get_total_items()} items):\n"
        for product in self.products:
            cart_str += f"  {product}\n"
        cart_str += f"Total: N{self.get_total_value()}"
        return cart_str