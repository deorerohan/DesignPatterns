import unittest
from Interfaces.create_order import CreateOrder
from Interfaces.ship_order import ShipOrder
from Interfaces.update_order import UpdateOrder

class TestCommand(unittest.TestCase):
    def test_CreateOrder(self):
        cmd = CreateOrder(list())
        cmd.execute()

    def test_ShipOrder(self):
        cmd = ShipOrder(list())
        cmd.execute()

    def test_UpdateOrder(self):
        cmd = UpdateOrder(["UpdateQuantity", "50"])
        cmd.execute()

if __name__ == '__main__':
    unittest.main()