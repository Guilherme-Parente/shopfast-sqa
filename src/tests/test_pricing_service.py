import pytest
from src.domain.pricing_service import PricingService
from src.models.order import Order
from src.models.coupon import Coupon
from src.models.payment import Payment
from src.domain.exceptions import BusinessException


def test_should_apply_discount_when_payment_is_valid():
    service = PricingService()

    order = Order(1000)
    coupon = Coupon(active=True, discount_rate=0.5)
    payment = Payment(authorized=True)

    result = service.calculate_final_amount(order, coupon, payment)

    assert result == 500


def test_should_fail_when_payment_not_authorized():
    service = PricingService()

    order = Order(1000)
    coupon = Coupon(active=True, discount_rate=0.5)
    payment = Payment(authorized=False)

    with pytest.raises(BusinessException):
        service.calculate_final_amount(order, coupon, payment)