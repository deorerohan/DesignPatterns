import unittest

from after_strategy.UpsStrategy import UpsStrategy
from after_strategy.FedExStrategy import FedExStrategy
from after_strategy.PostalStrategy import PostalStrategy
from after_strategy import Order, ShippingCost

class TestBeforeStrategy(unittest.TestCase):
    def test_FedexTest(self):
        order = Order.Order()
        strategy = FedExStrategy()
        cost_calculator = ShippingCost.ShippingCost(strategy)
        cost = cost_calculator.shipping_cost(order)
        self.assertEqual(cost, 3.5)

    def test_UPSTest(self):
        order = Order.Order()
        strategy = UpsStrategy()
        cost_calculator = ShippingCost.ShippingCost(strategy)
        cost = cost_calculator.shipping_cost(order)
        self.assertEqual(cost, 5.5)

    def test_PostalTest(self):
        order = Order.Order()
        strategy = PostalStrategy()
        cost_calculator = ShippingCost.ShippingCost(strategy)
        cost = cost_calculator.shipping_cost(order)
        self.assertEqual(cost, 4.5)

if __name__ == '__main__':
    unittest.main()