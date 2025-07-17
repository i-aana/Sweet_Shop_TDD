#file for data handling
import json
from sweet import Sweet
import os

#for data not found while loading data

class SweetDataNotFoundError(Exception):
    """Raised when the sweets.json file is not found."""
    pass

class DataPersistence:
    def __init__(self, filepath="sweets.json"):
        self.filepath = filepath

    #saving data
    def save_data(self, sweets: list[Sweet]):
        data = [sweet.to_dict() for sweet in sweets]
        with open(self.filepath, "w") as f:
            json.dump(data, f, indent=4)

    #getting data
    def load_data(self) -> list[Sweet]:
        if not os.path.exists(self.filepath):
            raise SweetDataNotFoundError("Sweet data file not found")
        with open(self.filepath, "r") as f:
            data = json.load(f)
        return [Sweet.from_dict(sweet_dict) for sweet_dict in data]