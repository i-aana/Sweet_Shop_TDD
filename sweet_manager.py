from sweet import Sweet
class SweetManager:
    def __init__(self):
        self.sweets = []

    def add_sweet(self, sweet: Sweet):
        if any(existing_sweet.name == sweet.name for existing_sweet in self.sweets):
            raise ValueError("Sweet with this name already exists")
        if sweet.quantity < 0:
            raise ValueError("Quantity must be non-negative")
        if sweet.price_per_kg < 0:
            raise ValueError("price must be non-negative")
        self.sweets.append(sweet)

    def delete_sweet(self, names: list[str] | str):
        if isinstance(names, str):
            names = [names]

        not_found = [name for name in names if name not in [s.name for s in self.sweets]]
        if not_found:
            raise ValueError("Sweet not found")

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

    def get_all_sweets(self):
        return self.sweets