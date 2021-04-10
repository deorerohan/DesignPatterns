from Interfaces import AbsCommand, AbsOrderCommand
class CreateOrder(AbsCommand.AbsCommand, AbsOrderCommand.AbsOrderCommand):
    name = 'CreateOrder'
    description = 'CreateOrder'

    def __init__(self, args) -> None:
        super().__init__()

    def execute(self):
        print('Created order')
