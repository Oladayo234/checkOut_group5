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
        with self.assertRaises(ValueError):
            self.product.set_price(-100)

    def test_that_product_quantity_cannot_be_negative(self):
        with self.assertRaises(ValueError):
            self.product.set_quantity(-5)

    def test_that_product_name_cannot_be_empty(self):
        with self.assertRaises(ValueError):
            self.product.set_name("")

    def test_that_product_price_must_be_a_number(self):
        with self.assertRaises(TypeError):
            self.product.set_price("abc")

    def test_that_product_name_must_be_string(self):
        with self.assertRaises(TypeError):
            Product(123, 1000, 5)

    def test_product_total_value_calculation(self):
        self.assertEqual(self.product.get_total_value(), 5000)

    def test_product_equality_by_name(self):
        product2 = Product("laptop", 500, 2) 
        self.assertEqual(self.product, product2)

    def test_product_inequality_different_names(self):
        product2 = Product("Mouse", 50, 1)
        self.assertNotEqual(self.product, product2)

    def test_name_whitespace_trimming(self):
        product = Product("  Trimmed  ", 100, 1)
        self.assertEqual(product.get_name(), "Trimmed")


if __name__ == '__main__':
    unittest.main()
