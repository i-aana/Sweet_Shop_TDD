import json
from sweet import Sweet

class DataPersistence:
    def __init__(self, filepath="sweets.json"):
        self.filepath = filepath

    def save_data(self, sweets: list[Sweet]):
        data = [sweet.to_dict() for sweet in sweets]
        with open(self.filepath, "w") as f:
            json.dump(data, f, indent=4)