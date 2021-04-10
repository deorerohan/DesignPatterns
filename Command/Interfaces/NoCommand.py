from Interfaces import AbsCommand

class NoCommand(AbsCommand.AbsCommand):
    def __init__(self, args) -> None:
        super().__init__()
        self._command = args[0]

    def execute(self):
        print(f'No command names {self._command}')