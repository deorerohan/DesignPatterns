from after_strategy import AbsStrategy

class PostalStrategy(AbsStrategy.AbsStrategy):
    def calculate(self, order):
        return 4.5