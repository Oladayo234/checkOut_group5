from datetime import datetime
from src.models.check_out import Cart

class Invoice:
    VAT_RATE = 0.075
    _counter = 0
    
    def __init__(self, cart: Cart):
        Invoice._counter += 1
        self.id = Invoice._counter
        self.date = datetime.now()
        self.cart = cart
        self.is_paid = False

    def validate_cart(self):
        if not self.cart.products:
            raise ValueError("Cart is empty. Cannot generate invoice.")

    def calculate_subtotal(self):
        total = 0
        for product in self.cart.products:
            total += product.price * product.quantity
        return total

    def calculate_vat(self):
        return self.calculate_subtotal() * self.VAT_RATE

    def calculate_total(self):
        return self.calculate_subtotal() + self.calculate_vat()

    def get_invoice(self):
        self.validate_cart()
        invoice = f"INVOICE #{self.id}\n"
        invoice += f"Date: {self.date.strftime('%Y-%m-%d %H:%M')}\n"
        invoice += "=" * 40 + "\n"
        invoice += "Products:\n"
        for product in self.cart.products:
            invoice += f"- {product.name}: N{product.price} x {product.quantity} = N{product.get_total_value()}\n"
        invoice += "=" * 40 + "\n"
        invoice += f"Subtotal: N{self.calculate_subtotal():.2f}\n"
        invoice += f"VAT ({self.VAT_RATE*100}%): N{self.calculate_vat():.2f}\n"
        invoice += f"TOTAL: N{self.calculate_total():.2f}\n"
        invoice += "\nPlease review and proceed to payment."
        return invoice

    def mark_as_paid(self):
        self.is_paid = True

    def get_receipt(self):
        if not self.is_paid:
            raise ValueError("Cannot generate receipt. Payment not confirmed.")
        self.validate_cart()
        return self.__str__()

    def __str__(self):
        receipt = f"RECEIPT\n"
        receipt += f"Invoice ID: {self.id}\n"
        receipt += f"Date: {self.date.strftime('%Y-%m-%d %H:%M')}\n"
        receipt += "=" * 40 + "\n"
        receipt += "Products:\n"
        for product in self.cart.products:
            receipt += f"- {product.name}: N{product.price} x {product.quantity} = N{product.get_total_value()}\n"
        receipt += "=" * 40 + "\n"
        receipt += f"Subtotal: N{self.calculate_subtotal():.2f}\n"
        receipt += f"VAT ({self.VAT_RATE*100}%): N{self.calculate_vat():.2f}\n"
        receipt += f"TOTAL: N{self.calculate_total():.2f}\n"
        receipt += f"Status: {'PAID' if self.is_paid else 'UNPAID'}\n"
        receipt += "\nThank you for shopping with us!"
        return receipt