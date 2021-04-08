import abc

class MyABC(metaclass=abc.ABCMeta):
    """Abstract base class definition"""
    #__metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def do_something(self,value):
        """Required method"""

    @abc.abstractproperty
    def some_property(self):
        """Required property"""



class MyInheritedABC(MyABC):
    def do_something(self, value):
        """Required method"""
        print(f'value : {value}')

    @property
    def some_property(self):
        """Required property"""
        print(f'property called')
        return 10

class MyBadInheritedABC(MyABC):
    pass


if __name__ == "__main__":
    obj = MyInheritedABC()
    obj.do_something(10)
    val = obj.some_property

    objBad = MyBadInheritedABC()
    objBad.do_something()
    val = objBad.some_property