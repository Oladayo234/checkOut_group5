import unittest
from src.models.check_out.Product import Product


class TestProduct(unittest.TestCase):
    def setUp(self):
        self.product = Product("Laptop", 1000, 5)

    def test_that_product_can_only_be_initialized_with_valid_values(self):
        self.assertEqual(self.product.get_name(), "Laptop")
        self.assertEqual(self.product.get_price(), 1000)
        self.assertEqual(self.product.get_quantity(), 5)

    def test_that_product_price_cannot_be_negative(self):
        with self.assertRaises(ValueError) as context:
            self.product.set_price(-100)
        self.assertEqual(str(context.exception), "Price cannot be negative")

    def test_that_product_quantity_cannot_be_negative(self):
        with self.assertRaises(ValueError) as context:
            self.product.set_quantity(-5)
        self.assertEqual(str(context.exception), "Quantity cannot be negative")

    def test_that_product_name_cannot_be_empty(self):
        with self.assertRaises(ValueError) as context:
            self.product.set_name("")
        self.assertEqual(str(context.exception), "Name cannot be empty")

    def test_that_product_price_must_be_a_digit(self):
        with self.assertRaises(ValueError) as context:
            self.product.set_price("abc")
        self.assertEqual(str(context.exception), "Value must be a digit")


if __name__ == '__main__':
    unittest.main()
