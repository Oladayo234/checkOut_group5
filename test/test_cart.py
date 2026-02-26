import unittest

from src.models.check_out.Cart import Cart
from src.models.check_out.Product import Product


class TestCart(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()
        self.apple = Product("Apple", 1.50, 3)
        self.bread = Product("Bread", 2.00, 1)
        self.milk = Product("Milk", 1.20, 2)

    def test_add_product_to_empty_cart(self):
        self.cart.add_product_to_cart(self.apple)
        self.assertTrue(self.apple in self.cart.products)

    def test_add_multiple_products(self):
        self.cart.add_product_to_cart(self.apple)
        self.cart.add_product_to_cart(self.bread)
        self.assertEqual(len(self.cart.products), 2)

    def test_add_duplicate_product(self):
        self.cart.add_product_to_cart(self.apple)
        self.cart.add_product_to_cart(self.apple)
        self.assertEqual(len(self.cart.products), 2)

    def test_remove_existing_product(self):
        self.cart.add_product_to_cart(self.apple)
        result = self.cart.remove_product_from_cart(self.apple)
        self.assertFalse(self.apple in self.cart.products)
        self.assertEqual(result, f"Item {self.apple.name} removed from cart")

    def test_remove_product_not_in_cart_raises_error(self):
        with self.assertRaises(ValueError):
            self.cart.remove_product_from_cart(self.apple)

    def test_remove_correct_product_when_multiple_exist(self):
        self.cart.add_product_to_cart(self.apple)
        self.cart.add_product_to_cart(self.bread)
        self.cart.remove_product_from_cart(self.apple)
        self.assertFalse(self.apple in self.cart.products)
        self.assertTrue(self.bread in self.cart.products)

    def test_find_existing_product_by_name(self):
        self.cart.add_product_to_cart(self.apple)
        result = self.cart.find_from_cart_by_name(self.apple)
        self.assertEqual(result, self.apple)

    def test_find_product_by_name_not_in_cart_returns_none(self):
        result = self.cart.find_from_cart_by_name(self.apple)
        self.assertEqual(result, None)

    def test_find_correct_product_by_name_among_multiple(self):
        self.cart.add_product_to_cart(self.apple)
        self.cart.add_product_to_cart(self.bread)
        result = self.cart.find_from_cart_by_name(self.bread)
        self.assertEqual(result, self.bread)

if __name__ == "__main__":
    unittest.main()