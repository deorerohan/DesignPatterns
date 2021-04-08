import unittest
from before_strategy import Order, ShippingCost, Shipper

class TestBeforeStrategy(unittest.TestCase):
    def test_FedexTest(self):
        order = Order.Order(Shipper.Shipper.Fedex)
        cost_calculator = ShippingCost.ShippingCost()
        cost = cost_calculator.shipping_cost(order)
        self.assertEqual(cost, 3.0)

    def test_UPSTest(self):
        order = Order.Order(Shipper.Shipper.UPS)
        cost_calculator = ShippingCost.ShippingCost()
        cost = cost_calculator.shipping_cost(order)
        self.assertEqual(cost, 4.0)

    def test_PostalTest(self):
        order = Order.Order(Shipper.Shipper.Postal)
        cost_calculator = ShippingCost.ShippingCost()
        cost = cost_calculator.shipping_cost(order)
        self.assertEqual(cost, 3.5)

if __name__ == '__main__':
    unittest.main()