from after_strategy import AbsStrategy

class UpsStrategy(AbsStrategy.AbsStrategy):
    def calculate(self, order):
        return 5.5