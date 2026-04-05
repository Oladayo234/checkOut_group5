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

    def test_calculate_vat_uses_class_constant(self):
        expected_vat = 6.50 * Invoice.VAT_RATE
        self.assertEqual(round(self.invoice.calculate_vat(), 4), round(expected_vat, 4))

    def test_calculate_total(self):
        expected = 6.50 + (6.50 * Invoice.VAT_RATE)
        self.assertEqual(round(self.invoice.calculate_total(), 4), round(expected, 4))

    def test_invoice_initially_unpaid(self):
        self.assertFalse(self.invoice.is_paid)

    def test_get_invoice_before_payment(self):
        invoice_text = self.invoice.get_invoice()
        self.assertIn("INVOICE", invoice_text)
        self.assertIn(str(self.invoice.id), invoice_text)
        self.assertIn("Apple", invoice_text)
        self.assertIn("Bread", invoice_text)
        self.assertIn("proceed to payment", invoice_text)

    def test_cannot_get_receipt_before_payment(self):
        with self.assertRaises(ValueError) as context:
            self.invoice.get_receipt()

    def test_mark_as_paid_changes_status(self):
        self.invoice.mark_as_paid()
        self.assertTrue(self.invoice.is_paid)

    def test_get_receipt_after_payment(self):
        self.invoice.mark_as_paid()
        receipt = self.invoice.get_receipt()
        self.assertIn("RECEIPT", receipt)
        self.assertIn("PAID", receipt)
        self.assertIn("Thank you", receipt)

    def test_receipt_contains_all_details(self):
        self.invoice.mark_as_paid()
        receipt = self.invoice.get_receipt()
        self.assertIn(str(self.invoice.id), receipt)
        self.assertIn("Apple", receipt)
        self.assertIn("Bread", receipt)
        self.assertIn("Subtotal", receipt)
        self.assertIn("VAT", receipt)
        self.assertIn("TOTAL", receipt)

    def test_vat_rate_as_class_constant(self):
        self.assertEqual(Invoice.VAT_RATE, 0.075)

    def test_empty_cart_invoice_validation(self):
        empty_cart = Cart()
        invoice = Invoice(empty_cart)
        with self.assertRaises(ValueError):
            invoice.get_invoice()


if __name__ == "__main__":
    unittest.main()