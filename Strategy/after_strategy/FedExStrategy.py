from after_strategy import AbsStrategy

class FedExStrategy(AbsStrategy.AbsStrategy):
    def calculate(self, order):
        return 3.5