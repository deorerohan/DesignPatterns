import abc

class AbsStrategy(metaclass = abc.ABCMeta):

    @abc.abstractclassmethod
    def calculate(self, order):
        """calculate abstract method"""