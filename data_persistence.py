import json
from sweet import Sweet
import os
class DataPersistence:
    def __init__(self, filepath="sweets.json"):
        self.filepath = filepath

    def save_data(self, sweets: list[Sweet]):
        data = [sweet.to_dict() for sweet in sweets]
        with open(self.filepath, "w") as f:
            json.dump(data, f, indent=4)

    def load_data(self) -> list[Sweet]:
        if not os.path.exists(self.filepath):
            return []
        with open(self.filepath, "r") as f:
            data = json.load(f)
        return [Sweet.from_dict(sweet_dict) for sweet_dict in data]