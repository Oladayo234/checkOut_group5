from src.models.check_out.Invoice import Invoice

def validate_name(name):
    if not isinstance(name, str):
        raise TypeError("Name must be a string")
    if name.strip() == "":
        raise ValueError("Name cannot be empty")
    return name.strip()

class Attendant:
    def __init__(self, name):
        self.name = validate_name(name)
        self.invoices = []

    def create_invoice(self, cart):
        if not cart.products:
            raise ValueError("Cart is empty. Cannot generate invoice.")
        invoice = Invoice(cart)
        self.invoices.append(invoice)
        return invoice

    def process_payment(self, invoice_id):
        invoice = self.get_invoice_by_id(invoice_id)
        if not invoice:
            raise ValueError(f"Invoice {invoice_id} not found")
        invoice.mark_as_paid()
        return invoice

    def get_invoice_by_id(self, invoice_id):
        for invoice in self.invoices:
            if invoice.id == invoice_id:
                return invoice
        return None

    def get_invoices(self):
        return self.invoices.copy()

    def get_paid_invoices(self):
        return [invoice for invoice in self.invoices if invoice.is_paid]

    def get_unpaid_invoices(self):
        return [invoice for invoice in self.invoices if not invoice.is_paid]

    def get_name(self):
        return self.name