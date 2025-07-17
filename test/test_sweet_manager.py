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

    def test_delete_single_sweet(self):
        sweet = Sweet("Ladoo", "Dry", 10, 15.0)
        self.manager.add_sweet(sweet)

        self.manager.delete_sweet(["Ladoo"])
        sweets = self.manager.get_all_sweets()

        self.assertEqual(len(sweets), 0)

    def test_delete_multiple_sweets(self):
        sweet1 = Sweet("Ladoo", "Dry", 10, 15.0)
        sweet2 = Sweet("Barfi", "Milk", 8, 20.0)
        sweet3 = Sweet("Jalebi", "Sugar", 12, 10.0)

        self.manager.add_sweet(sweet1)
        self.manager.add_sweet(sweet2)
        self.manager.add_sweet(sweet3)

        self.manager.delete_sweet(["Barfi"])
        self.manager.delete_sweet(["Jalebi"])

        sweets = self.manager.get_all_sweets()
        self.assertEqual(len(sweets), 1)
        self.assertEqual(sweets[0].name, "Ladoo")

    def test_delete_multiple_sweets_in_one_call(self):
        sweet1 = Sweet("Ladoo", "Dry", 10, 15.0)
        sweet2 = Sweet("Barfi", "Milk", 8, 20.0)
        sweet3 = Sweet("Jalebi", "Sugar", 12, 10.0)

        self.manager.add_sweet(sweet1)
        self.manager.add_sweet(sweet2)
        self.manager.add_sweet(sweet3)

        self.manager.delete_sweet(["Barfi", "Jalebi"])

        sweets = self.manager.get_all_sweets()
        self.assertEqual(len(sweets), 1)
        self.assertEqual(sweets[0].name, "Ladoo")

    def test_delete_nonexistent_sweet_raises_error(self):
        with self.assertRaises(ValueError) as context:
            self.manager.delete_sweet("NonexistentSweet")
        self.assertEqual(str(context.exception), "Sweet not found")

    def test_update_sweet(self):
        sweet = Sweet("Ladoo", "Dry", 10, 15.0)
        self.manager.add_sweet(sweet)

        # Now update the sweet
        self.manager.update_sweet("Ladoo", new_category="Milk", new_quantity=20, new_price=18.0)

        sweets = self.manager.get_all_sweets()
        self.assertEqual(len(sweets), 1)
        updated_sweet = sweets[0]
        self.assertEqual(updated_sweet.name, "Ladoo")  # Name stays same
        self.assertEqual(updated_sweet.category, "Milk")  # category updated
        self.assertEqual(updated_sweet.quantity, 20)  # Quantity updated
        self.assertEqual(updated_sweet.price_per_kg, 18.0)  # Price updated

    def test_update_nonexistent_sweet_raises_error(self):
        with self.assertRaises(ValueError) as context:
            self.manager.update_sweet("Nonexistentent", new_category="Milk")

        self.assertEqual(str(context.exception), "Sweet not found")

    def test_update_sweet_with_negative_quantity_raises_error(self):
        sweet = Sweet("Ladoo", "Dry", 10, 15.0)
        self.manager.add_sweet(sweet)

        with self.assertRaises(ValueError) as context:
            self.manager.update_sweet("Ladoo","Dry", -5, 20.0)
        self.assertEqual(str(context.exception), "Quantity must be non-negative")

    def test_update_sweet_with_negative_price_raises_error(self):
        sweet = Sweet("Ladoo", "Dry", 10, 15.0)
        self.manager.add_sweet(sweet)

        with self.assertRaises(ValueError) as context:
            self.manager.update_sweet("Ladoo", "Dry" ,5, -20.0)
        self.assertEqual(str(context.exception), "price must be non-negative")

    def test_get_all_sweets_returns_all(self):
        sweet1 = Sweet("Ladoo", "Milk", 10, 200.0)
        sweet2 = Sweet("Barfi", "Milk", 5, 250.0)
        self.manager.add_sweet(sweet1)
        self.manager.add_sweet(sweet2)

        sweets = self.manager.get_all_sweets()
        self.assertEqual(len(sweets), 2)
        self.assertEqual(sweets[0].name, "Ladoo")
        self.assertEqual(sweets[1].name, "Barfi")

    def test_search_by_name_returns_matching_sweets(self):
        self.manager.add_sweet(Sweet("Kaju Katli", "Dryfruit", 10, 300))
        self.manager.add_sweet(Sweet("Kaju Roll", "Dryfruit", 5, 250))
        self.manager.add_sweet(Sweet("Chocolate Barfi", "Milk", 8, 200))
        self.manager.add_sweet(Sweet("Kesar Kaju", "Dryfruit", 6, 350))
        self.manager.add_sweet(Sweet("Ladoo", "Milk", 15, 100))  # Irrelevant

        result = self.manager.search_by_name("kaju")

        self.assertEqual(len(result), 2)

    def test_filter_by_price_range_returns_correct_sweets(self):
        self.manager.add_sweet(Sweet("Ladoo", "Milk", 10, 200))
        self.manager.add_sweet(Sweet("Barfi", "Milk", 5, 400))
        result = self.manager.filter_by_price_range(100, 300)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].name, "Ladoo")

    def test_search_by_category_returns_matching_sweets(self):
        self.manager.add_sweet(Sweet("Kaju Katli", "Dryfruit", 10, 300))
        self.manager.add_sweet(Sweet("Ladoo", "Milk", 20, 100))
        self.manager.add_sweet(Sweet("Kaju Roll", "Dryfruit", 5, 250))
        self.manager.add_sweet(Sweet("Barfi", "Milk", 15, 150))

        result = self.manager.search_by_category("Dryfruit")
        self.assertEqual(len(result), 2)
        self.assertTrue(all(sweet.category == "Dryfruit" for sweet in result))
        self.assertEqual(result[0].name, "Kaju Katli")
        self.assertEqual(result[1].name, "Kaju Roll")

if __name__ == "__main__":
    unittest.main()  # looks for all test_* methods and runs them.