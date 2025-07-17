import unittest
from sweet import Sweet
from sweet_manager import SweetManager
class TestSweetManager(unittest.TestCase):#inheriting from unittest.TestCase
    def setUp(self):#creates fresh SweetManager each time; ENSURES TESTS ARE INDEPENDENT
        self.manager = SweetManager()

    def test_add_a_sweet(self):
        sweet = Sweet("Sonpapdi", "Dry", 10, 15.0)
        self.manager.add_sweet(sweet)# calling add sweet method to add sweet
        sweets = self.manager.get_all_sweets()# fetching sweets

        self.assertEqual(len(sweets), 1)
        self.assertEqual(sweets[0].name, "Sonpapdi")

    def test_add_multiple_sweets(self):
        sweet1 = Sweet("Ladoo", "Dry", 12, 30.0)
        sweet2 = Sweet("Barfi", "Milk", 5, 20.0)
        self.manager.add_sweet(sweet1)
        self.manager.add_sweet(sweet2)

        sweets = self.manager.get_all_sweets()

        self.assertEqual(len(sweets), 2)  # This should FAIL currently
        self.assertEqual(sweets[1].name, "Barfi")  # Optional extra check

    def test_adding_duplicate_sweet_raises_error(self):
        sweet1 = Sweet("Ladoo", "Desi", 5, 200)
        sweet2 = Sweet("Ladoo", "Festival", 10, 250)

        self.manager.add_sweet(sweet1)

        with self.assertRaises(ValueError) as context:
            self.manager.add_sweet(sweet2)

        self.assertEqual(str(context.exception), "Sweet with this name already exists")

    def test_adding_sweet_with_negative_quantity_raises_error(self):
        sweet = Sweet("Kaju Katli", "Nut", -5, 400)
        with self.assertRaises(ValueError) as context:
            self.manager.add_sweet(sweet)
        self.assertEqual(str(context.exception), "Quantity must be non-negative")

    def test_adding_sweet_with_negative_price_raises_error(self):
        sweet = Sweet("Barfi", "Regular", 2, -250)
        with self.assertRaises(ValueError) as context:
            self.manager.add_sweet(sweet)
        self.assertEqual(str(context.exception), "price must be non-negative")

if __name__ == "__main__":
    unittest.main()  # looks for all test_* methods and runs them.