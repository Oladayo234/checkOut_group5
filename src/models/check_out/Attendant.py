from src.models.check_out.Invoice import Invoice
class Attendant:

    def __init__(self, name):
        self.name = self.__validate_name(name)
        self.invoices = []

    def create_invoice(self, cart):
        if not cart.products:
            raise ValueError("Cart is empty. Cannot generate invoice.")
        invoice = Invoice(cart)
        self.invoices.append(invoice)
        return invoice

    def get_invoice(self, cart):
        if not cart.products:
            raise ValueError("Cart is empty. Cannot generate invoice.")
        invoice = Invoice(cart)
        self.invoices.append(invoice)
        return invoice

    def get_name(self):
        return self.name

    def __validate_name(self, name):
        if name.strip() == "":
            raise ValueError("Name cannot be empty")
        return name