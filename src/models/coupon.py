class Coupon:
    def __init__(self, active: bool, discount_rate: float):
        self.active = active
        self.discount_rate = discount_rate

    def is_active(self) -> bool:
        return self.active

    def is_applicable_to(self, order) -> bool:
        return order.total > 0