from before_strategy import Order, ShippingCost, Shipper

order = Order.Order(Shipper.Shipper.Fedex)
cost_calculator = ShippingCost.ShippingCost()
cost = cost_calculator.shipping_cost(order)
assert cost == 3.0

order = Order.Order(Shipper.Shipper.UPS)
cost_calculator = ShippingCost.ShippingCost()
cost = cost_calculator.shipping_cost(order)
assert cost == 4.0

order = Order.Order(Shipper.Shipper.Postal)
cost_calculator = ShippingCost.ShippingCost()
cost = cost_calculator.shipping_cost(order)
assert cost == 3.5

print('wrong test passed')