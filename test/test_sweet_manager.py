import unittest
from sweet import Sweet
from sweet_manager import SweetManager
import os
import json
from data_persistence import DataPersistence
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

    def test_sort_by_name_alphabetical(self):
        self.manager.add_sweet(Sweet("Barfi", "Milk", 8, 200))
        self.manager.add_sweet(Sweet("Ladoo", "Milk", 5, 150))
        self.manager.add_sweet(Sweet("Kaju Katli", "Dryfruit", 10, 300))

        sorted_sweets = self.manager.sort_by_name()
        self.assertEqual([s.name for s in sorted_sweets], ["Barfi", "Kaju Katli", "Ladoo"])

    def test_sort_by_category_alphabetical(self):
        self.manager.add_sweet(Sweet("Barfi", "Milk", 8, 200))
        self.manager.add_sweet(Sweet("Ladoo", "Sugar", 5, 150))
        self.manager.add_sweet(Sweet("Kaju Katli", "Dryfruit", 10, 300))

        sorted_sweets = self.manager.sort_by_category()
        self.assertEqual([s.category for s in sorted_sweets], ["Dryfruit", "Milk", "Sugar"])

    def test_purchase_sweet_reduces_quantity(self):
        self.manager.add_sweet(Sweet("Gulab Jamun", "Milk", 20, 150))
        self.manager.purchase_sweet("Gulab Jamun", 5)
        self.assertEqual(self.manager.sweets[0].quantity, 15)

    def test_purchase_more_than_stock_raises_error(self):
        self.manager.add_sweet(Sweet("Kaju Katli", "Dryfruit", 3, 300))
        with self.assertRaises(ValueError) as context:
            self.manager.purchase_sweet("Kaju Katli", 5)
        self.assertEqual(str(context.exception), "Not enough stock")

    def test_restock_sweet_increases_quantity(self):
        sweet = Sweet("Rasgulla", "Syrup-based", 10, 150)
        self.manager.add_sweet(sweet)

        self.manager.restock_sweet("Rasgulla", 5)

        self.assertEqual(sweet.quantity, 15)

    def test_restock_nonexistent_sweet_raises_error(self):
        with self.assertRaises(ValueError) as context:
            self.manager.restock_sweet("Nonexistent", 10)
        self.assertEqual(str(context.exception), "Sweet not found")

    def test_restock_with_invalid_quantity_raises_error(self):
        sweet = Sweet("Rasgulla", "Syrup-based", 10, 150)
        self.manager.add_sweet(sweet)

        with self.assertRaises(ValueError) as context:
            self.manager.restock_sweet("Rasgulla", 0)
        self.assertEqual(str(context.exception), "Quantity must be greater than zero")

#storing and retrieving sweets info.
class TestDataPersistence(unittest.TestCase):

    def test_save_data_creates_valid_json_file(self):
        test_file = "test_sweets_save.json"

        # Step 1: Create manager and add a sweet object
        manager = SweetManager()
        manager.sweets = [
            Sweet(name="Kaju Katli", category="Dry Fruit", quantity=5, price_per_kg=1000)
        ]

        # Print debug info
        # print("\n--- Running test_save_data_creates_valid_json_file ---")
        # print("🧁 manager.sweets =", manager.sweets)
        # print("📦 Types in manager.sweets =", [type(s) for s in manager.sweets])
        # for s in manager.sweets:
        #     print(f"🔎 {s} (type={type(s)})")

        # Step 2: Save to file
        dp = DataPersistence(test_file)
        dp.save_data(manager.sweets)

        # Step 3: Assert file created
        self.assertTrue(os.path.exists(test_file), "JSON file not created!")

        # Step 4: Load and verify contents
        with open(test_file, 'r') as f:
            data = json.load(f)

        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 1)

        sweet_data = data[0]
        self.assertEqual(sweet_data['name'], "Kaju Katli")
        self.assertEqual(sweet_data['category'], "Dry Fruit")
        self.assertEqual(sweet_data['quantity'], 5)
        self.assertEqual(sweet_data['price_per_kg'], 1000)

        # Step 5: Cleanup

        os.remove(test_file)

    def test_load_data_reads_valid_json_file(self):
        test_file = "test_sweets_load.json"

        # Step 1: Prepare a dummy JSON file
        sample_data = [
            {
                "name": "Rasgulla",
                "category": "Syrupy",
                "quantity": 10,
                "price_per_kg": 600
            }
        ]
        with open(test_file, "w") as f:
            json.dump(sample_data, f, indent=4)

        # Step 2: Load using DataPersistence
        dp = DataPersistence(test_file)
        sweets = dp.load_data()

        # Step 3: Assert content
        self.assertEqual(len(sweets), 1)
        sweet = sweets[0]
        self.assertIsInstance(sweet, Sweet)
        self.assertEqual(sweet.name, "Rasgulla")
        self.assertEqual(sweet.category, "Syrupy")
        self.assertEqual(sweet.quantity, 10)
        self.assertEqual(sweet.price_per_kg, 600)

        # Step 4: Clean up
        os.remove(test_file)

    def test_load_data_handles_nonexistent_file(self):
        test_file = "nonexistent_file.json"

        # Ensure file does not exist
        if os.path.exists(test_file):
            os.remove(test_file)

        dp = DataPersistence(test_file)
        result = dp.load_data()

        # Assert that it returns an empty list, not an exception
        self.assertEqual(result, "Sweet data file not found")


if __name__ == "__main__":
    unittest.main()  # looks for all test_* methods and runs them.