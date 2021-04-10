from Interfaces import AbsCommand, AbsOrderCommand
class UpdateOrder(AbsCommand.AbsCommand, AbsOrderCommand.AbsOrderCommand):
    name = 'UpdateQuantity'
    description = 'UpdateQuantity number'
    
    def __init__(self, args) -> None:
        super().__init__()
        self.newqty = args[1]

    def execute(self):
        oldqty = 5
        print('Update database')

        print(f'Logging : Update quantity from {oldqty} to {self.newqty}')