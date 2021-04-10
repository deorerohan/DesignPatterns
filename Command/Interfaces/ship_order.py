from Interfaces import AbsCommand, AbsOrderCommand
class ShipOrder(AbsCommand.AbsCommand, AbsOrderCommand.AbsOrderCommand):
    name = 'ShipOrder'
    description = 'ShipOrder'

    def __init__(self, args) -> None:
        super().__init__()

    def execute(self):
        print('Shipped order')