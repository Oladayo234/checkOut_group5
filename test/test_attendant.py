import unittest
from src.models.check_out.Attendant import Attendant
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

    def test_get_invoice_returns_invoice(self):
        invoice = self.attendant.get_invoice(self.cart)
        self.assertEqual(invoice.cart, self.cart)

    def test_get_invoice_empty_cart_raises_error(self):
        with self.assertRaises(ValueError):
            self.attendant.get_invoice(Cart())

    def test_get_invoice_stores_invoice_in_history(self):
        invoice = self.attendant.get_invoice(self.cart)
        self.assertTrue(invoice in self.attendant.invoices)

    def test_attendant_name_is_set(self):
        self.assertEqual(self.attendant.get_name(), "Christian")

    def test_attendant_empty_name_raises_error(self):
        with self.assertRaises(ValueError):
            Attendant("")

    def test_attendant_blank_name_raises_error(self):
        with self.assertRaises(ValueError):
            Attendant("   ")

    def test_invoice_history_grows_with_each_invoice(self):
        cart2 = Cart()
        cart2.add_product_to_cart(self.apple)
        self.attendant.get_invoice(self.cart)
        self.attendant.get_invoice(cart2)
        self.assertEqual(len(self.attendant.invoices), 2)

    def test_invoice_history_starts_empty(self):
        new_attendant = Attendant("Semicolon")
        self.assertEqual(len(new_attendant.invoices), 0)

if __name__ == "__main__":
    unittest.main()
