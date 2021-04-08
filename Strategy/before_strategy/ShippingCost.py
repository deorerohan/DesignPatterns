from before_strategy.Shipper import Shipper

class ShippingCost():
    def shipping_cost(self, order):
        if order.shipper == Shipper.Fedex:
            return self._fedex_cost(order)
        elif order.shipper == Shipper.UPS:
            return self._ups_cost(order)
        elif order.shipper == Shipper.Postal:
            return self._postal_cost(order)
        else:
            raise ValueError(f'Invalid shipper {order.shipper}')

    def _fedex_cost(self, order):
        return 3

    def _ups_cost(self, order):
        return 4

    def _postal_cost(self, order):
        return 3.5