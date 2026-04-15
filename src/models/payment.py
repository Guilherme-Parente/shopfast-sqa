class Payment:
    def __init__(self, authorized: bool):
        self.authorized = authorized

    def is_authorized(self) -> bool:
        return self.authorized