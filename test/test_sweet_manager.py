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

if __name__ == "__main__":
    unittest.main()  # looks for all test_* methods and runs them.