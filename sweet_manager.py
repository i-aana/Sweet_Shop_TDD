from sweet import Sweet
class SweetManager:
    def __init__(self):
        self.sweets = []

    def add_sweet(self, sweet: Sweet):
        self.sweets.append(sweet)

    def get_all_sweets(self):
        return self.sweets