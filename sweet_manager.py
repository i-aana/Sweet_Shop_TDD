from sweet import Sweet
from data_persistence import DataPersistence
class SweetManager:
    def __init__(self):
        self.sweets = []
        self.data_persistence = DataPersistence()

    def add_sweet(self, sweet: Sweet):
        if any(existing_sweet.name == sweet.name for existing_sweet in self.sweets):
            raise ValueError("Sweet with this name already exists")
        if sweet.quantity < 0:
            raise ValueError("Quantity must be non-negative")
        if sweet.price_per_kg < 0:
            raise ValueError("price must be non-negative")
        self.sweets.append(sweet)
        self.data_persistence.save_data(self.sweets)

    def delete_sweet(self, names: list[str] | str):
        if isinstance(names, str):
            names = [names]

        # Gather all current sweet names
        existing_names = {s.name for s in self.sweets}

        # Identify names that are not in the list
        not_found = [name for name in names if name not in existing_names]
        if not_found:
            raise ValueError("Sweet not found")

        # Delete all matching sweets
        self.sweets = [sweet for sweet in self.sweets if sweet.name not in names]

    def update_sweet(self, name, new_category=None, new_quantity=None, new_price=None):
        for sweet in self.sweets:
            if sweet.name == name:
                if new_quantity is not None:
                    if new_quantity < 0:
                        raise ValueError("Quantity must be non-negative")
                    sweet.quantity = new_quantity
                if new_price is not None:
                    if new_price < 0:
                        raise ValueError("price must be non-negative")
                    sweet.price_per_kg = new_price
                if new_category is not None:
                    sweet.category = new_category
            return
        raise ValueError("Sweet not found")

    def search_by_name(self, name: str) -> list[Sweet]:
        name = name.strip().lower()
        return [sweet for sweet in self.sweets if sweet.name.lower().startswith(name)]

    def filter_by_price_range(self, min_price: float, max_price: float) -> list[Sweet]:
        return [sweet for sweet in self.sweets if min_price <= sweet.price_per_kg <= max_price]

    def search_by_category(self, category: str) -> list[Sweet]:
        return [sweet for sweet in self.sweets if sweet.category.lower() == category.lower()]

    def sort_by_name(self) -> list[Sweet]:
        return sorted(self.sweets, key=lambda sweet: sweet.name.lower())

    def sort_by_category(self) -> list[Sweet]:
        return sorted(self.sweets, key=lambda sweet: sweet.category.lower())

    def purchase_sweet(self, name: str, quantity: int):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero")

        for sweet in self.sweets:
            if sweet.name.lower() == name.lower():
                if sweet.quantity < quantity:
                    raise ValueError("Not enough stock")
                sweet.quantity -= quantity
                return
        raise ValueError("Sweet not found")

    def restock_sweet(self, name: str, quantity: int):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero")

        for sweet in self.sweets:
            if sweet.name.lower() == name.lower():
                sweet.quantity += quantity
                return
        raise ValueError("Sweet not found")

    def get_all_sweets(self):
        return self.sweets