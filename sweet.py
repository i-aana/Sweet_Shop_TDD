#data container class
class Sweet:
    def __init__(self,name: str,category: str,quantity: int,price_per_kg :float):
        self.name =name
        self.category=category
        self.quantity =quantity
        self.price_per_kg=price_per_kg

    def to_dict(self):
        return {
            "name": self.name,
            "category": self.category,
            "quantity": self.quantity,
            "price_per_kg": self.price_per_kg
        }

    @staticmethod
    def from_dict(data: dict):
        return Sweet(
            name=data["name"],
            category=data["category"],
            quantity=data["quantity"],
            price_per_kg=data["price_per_kg"]
        )