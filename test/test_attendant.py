import unittest
from src.models.check_out.Attendant import Attendant, validate_name
from src.models.check_out.Cart import Cart
from src.models.check_out.Product import Product

class TestAttendant(unittest.TestCase):

    def setUp(self):
        self.attendant = Attendant("Christian")
        self.cart = Cart()
        self.apple = Product("Apple", 1.50, 3)
        self.bread = Product("Bread", 2.00, 1)
        self.cart.add_product_to_cart(self.apple)
        self.cart.add_product_to_cart(self.bread)

    def test_create_invoice_returns_invoice(self):
        invoice = self.attendant.create_invoice(self.cart)
        self.assertEqual(invoice.cart, self.cart)

    def test_create_invoice_empty_cart_raises_error(self):
        with self.assertRaises(ValueError):
            self.attendant.create_invoice(Cart())

    def test_create_invoice_stores_invoice_in_history(self):
        invoice = self.attendant.create_invoice(self.cart)
        self.assertTrue(invoice in self.attendant.invoices)

    def test_attendant_name_is_set(self):
        self.assertEqual(self.attendant.get_name(), "Christian")

    def test_attendant_empty_name_raises_error(self):
        with self.assertRaises(ValueError):
            Attendant("")

    def test_attendant_blank_name_raises_error(self):
        with self.assertRaises(ValueError):
            Attendant("   ")

    def test_attendant_non_string_name_raises_error(self):
        with self.assertRaises(TypeError):
            Attendant(123)

    def test_invoice_history_grows_with_each_invoice(self):
        cart2 = Cart()
        cart2.add_product_to_cart(self.apple)
        self.attendant.create_invoice(self.cart)
        self.attendant.create_invoice(cart2)
        self.assertEqual(len(self.attendant.invoices), 2)

    def test_invoice_history_starts_empty(self):
        new_attendant = Attendant("Semicolon")
        self.assertEqual(len(new_attendant.invoices), 0)

    def test_process_payment_marks_invoice_as_paid(self):
        invoice = self.attendant.create_invoice(self.cart)
        paid_invoice = self.attendant.process_payment(invoice.id)
        self.assertTrue(paid_invoice.is_paid)
        self.assertEqual(paid_invoice, invoice)

    def test_process_payment_invalid_id_raises_error(self):
        with self.assertRaises(ValueError):
            self.attendant.process_payment(999)

    def test_get_invoice_by_id_returns_correct_invoice(self):
        invoice = self.attendant.create_invoice(self.cart)
        found = self.attendant.get_invoice_by_id(invoice.id)
        self.assertEqual(found, invoice)

    def test_get_invoice_by_id_not_found_returns_none(self):
        found = self.attendant.get_invoice_by_id(999)
        self.assertIsNone(found)

    def test_get_invoices_returns_copy(self):
        invoice = self.attendant.create_invoice(self.cart)
        invoices = self.attendant.get_invoices()
        self.assertEqual(len(invoices), 1)
        self.assertIsNot(invoices, self.attendant.invoices)  # Should be a copy

    def test_get_paid_invoices_filters_correctly(self):
        invoice1 = self.attendant.create_invoice(self.cart)
        cart2 = Cart()
        cart2.add_product_to_cart(self.apple)
        invoice2 = self.attendant.create_invoice(cart2)
        
        self.attendant.process_payment(invoice1.id)
        
        paid_invoices = self.attendant.get_paid_invoices()
        self.assertEqual(len(paid_invoices), 1)
        self.assertEqual(paid_invoices[0], invoice1)

    def test_get_unpaid_invoices_filters_correctly(self):
        invoice1 = self.attendant.create_invoice(self.cart)
        cart2 = Cart()
        cart2.add_product_to_cart(self.apple)
        invoice2 = self.attendant.create_invoice(cart2)
        
        self.attendant.process_payment(invoice1.id)
        
        unpaid_invoices = self.attendant.get_unpaid_invoices()
        self.assertEqual(len(unpaid_invoices), 1)
        self.assertEqual(unpaid_invoices[0], invoice2)

    def test_attendant_repr(self):
        attendant_repr = repr(self.attendant)
        self.assertIn("Attendant", attendant_repr)
        self.assertIn("Christian", attendant_repr)
        self.assertIn("invoices=0", attendant_repr)

    def test_validate_name_utility_function(self):
        self.assertEqual(validate_name("  Test  "), "Test")
        with self.assertRaises(ValueError):
            validate_name("")
        with self.assertRaises(TypeError):
            validate_name(123)

if __name__ == "__main__":
    unittest.main()
