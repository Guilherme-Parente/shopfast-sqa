from src.domain.exceptions import BusinessException


class PricingService:

    def calculate_final_amount(self, order, coupon, payment):
        self._ensure_payment_approved(payment)
        self._ensure_coupon_valid(coupon, order)

        return self._apply_discount(order, coupon)

    def _ensure_payment_approved(self, payment):
        if payment is None or not payment.is_authorized():
            raise BusinessException("Pagamento não autorizado")

    def _ensure_coupon_valid(self, coupon, order):
        if coupon is None or not coupon.is_active():
            raise BusinessException("Cupom inválido")

        if not coupon.is_applicable_to(order):
            raise BusinessException("Cupom não aplicável")

    def _apply_discount(self, order, coupon):
        return order.apply_discount(coupon.discount_rate)