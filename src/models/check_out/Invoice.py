from datetime import datetime
from src.models.check_out import Cart

VAT_RATE = 0.075
class Invoice:
    _counter = 0
    def __init__(self, cart: Cart):
        Invoice._counter += 1
        self.id = Invoice._counter
        self.date = datetime.now()
        self.cart = cart

    def validate_cart(self):
        if not self.cart.products:
            raise ValueError("Cart is empty. Cannot generate invoice.")

    def calculate_subtotal(self):
        total = 0
        for product in self.cart.products:
            if product.price < 0:
                raise ValueError(f"Invalid price for {product.name}")
            total += product.price * product.quantity
        return total

    def calculate_vat(self):
        return self.calculate_subtotal() * VAT_RATE

    def calculate_total(self):
        return self.calculate_subtotal() + self.calculate_vat()

    def get_receipt(self):
        if not self.cart.products:
            raise ValueError("Cart is empty. Cannot generate receipt.")
        return self.__str__()

    def __str__(self):
        receipt = f"Invoice ID: {self.id}\nDate: {self.date.strftime('%Y-%m-%d %H:%M')}\n"
        receipt += "Products:\n"
        for product in self.cart.products:
            receipt += f"- {product.name}: N{product.price} x {product.quantity}\n"
        receipt += f"Subtotal: N{self.calculate_subtotal()}\n"
        receipt += f"VAT: N{self.calculate_vat()}\n"
        receipt += f"Total: N{self.calculate_total()}\n"
        receipt += "Thank you for shopping with us!"
        return receipt