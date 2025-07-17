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

    def get_all_sweets(self):
        return self.sweets