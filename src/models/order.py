class Order:
    def __init__(self, total: float):
        self.total = total

    def apply_discount(self, discount_rate: float) -> float:
        return self.total * (1 - discount_rate)