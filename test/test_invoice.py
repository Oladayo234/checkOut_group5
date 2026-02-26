import unittest

from src.models.check_out.Cart import Cart
from src.models.check_out.Invoice import Invoice
from src.models.check_out.Product import Product


class TestInvoice(unittest.TestCase):

    def setUp(self):
        self.cart = Cart()
        self.apple = Product("Apple", 1.50, 3)
        self.bread = Product("Bread", 2.00, 1)
        self.cart.add_product_to_cart(self.apple)
        self.cart.add_product_to_cart(self.bread)
        self.invoice = Invoice(self.cart)

    def test_invoice_id_increments(self):
        invoice2 = Invoice(Cart())
        self.assertEqual(invoice2.id, self.invoice.id + 1)

    def test_validate_empty_cart_raises_error(self):
        invoice = Invoice(Cart())
        with self.assertRaises(ValueError):
            invoice.validate_cart()

    def test_calculate_subtotal(self):
        self.assertEqual(self.invoice.calculate_subtotal(), 6.50)

    def test_calculate_subtotal_negative_price_raises_error(self):
        with self.assertRaises(ValueError):
            Product("Bad", -1.00, 1)

    def test_calculate_vat(self):
        self.assertEqual(round(self.invoice.calculate_vat(), 4), round(6.50 * 0.075, 4))

    def test_calculate_total(self):
        expected = 6.50 + (6.50 * 0.075)
        self.assertEqual(round(self.invoice.calculate_total(), 4), round(expected, 4))

    def test_get_receipt_contains_id(self):
        self.assertTrue(str(self.invoice.id) in self.invoice.get_receipt())

    def test_get_receipt_contains_product_names(self):
        receipt = self.invoice.get_receipt()
        self.assertTrue("Apple" in receipt)
        self.assertTrue("Bread" in receipt)

    def test_get_receipt_contains_totals(self):
        receipt = self.invoice.get_receipt()
        self.assertTrue("Subtotal" in receipt)
        self.assertTrue("VAT" in receipt)
        self.assertTrue("Total" in receipt)


if __name__ == "__main__":
    unittest.main()