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

    def test_add_duplicate_product_increases_quantity(self):
        """Test that adding same product increases quantity instead of duplicating"""
        self.cart.add_product_to_cart(self.apple)
        apple2 = Product("Apple", 1.50, 2)
        self.cart.add_product_to_cart(apple2)
        
        self.assertEqual(len(self.cart.products), 1)
        found_apple = self.cart.find_from_cart_by_name(self.apple)
        self.assertEqual(found_apple.get_quantity(), 5)

    def test_case_insensitive_duplicate_detection(self):
        """Test that 'Apple' and 'apple' are treated as same product"""
        self.cart.add_product_to_cart(self.apple)
        apple_lower = Product("apple", 1.50, 1)
        self.cart.add_product_to_cart(apple_lower)
        
        self.assertEqual(len(self.cart.products), 1)
        found_apple = self.cart.find_from_cart_by_name(self.apple)
        self.assertEqual(found_apple.get_quantity(), 4)

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

    def test_find_existing_product_by_name_case_insensitive(self):
        self.cart.add_product_to_cart(self.apple)
        apple_search = Product("APPLE", 0, 0)
        result = self.cart.find_from_cart_by_name(apple_search)
        self.assertEqual(result.get_name(), "Apple")

    def test_find_product_by_name_not_in_cart_returns_none(self):
        result = self.cart.find_from_cart_by_name(self.apple)
        self.assertEqual(result, None)

    def test_find_correct_product_by_name_among_multiple(self):
        self.cart.add_product_to_cart(self.apple)
        self.cart.add_product_to_cart(self.bread)
        result = self.cart.find_from_cart_by_name(self.bread)
        self.assertEqual(result, self.bread)

    def test_cart_total_items_count(self):
        self.cart.add_product_to_cart(self.apple)
        self.cart.add_product_to_cart(self.bread)
        self.assertEqual(self.cart.get_total_items(), 4)

    def test_cart_total_value_calculation(self):
        self.cart.add_product_to_cart(self.apple)
        self.cart.add_product_to_cart(self.bread)
        self.assertEqual(self.cart.get_total_value(), 6.50)

    def test_cart_is_empty_initially(self):
        self.assertTrue(self.cart.is_empty())

    def test_cart_is_not_empty_after_adding_product(self):
        self.cart.add_product_to_cart(self.apple)
        self.assertFalse(self.cart.is_empty())

    def test_clear_cart_removes_all_products(self):
        self.cart.add_product_to_cart(self.apple)
        self.cart.add_product_to_cart(self.bread)
        self.cart.clear_cart()
        self.assertTrue(self.cart.is_empty())

    def test_cart_repr(self):
        self.cart.add_product_to_cart(self.apple)
        cart_repr = repr(self.cart)
        self.assertIn("Cart", cart_repr)
        self.assertIn("products=1", cart_repr)

if __name__ == "__main__":
    unittest.main()