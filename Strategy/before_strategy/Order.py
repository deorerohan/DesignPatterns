import abc

class Order(metaclass=abc.ABCMeta):
    def __init__(self, shipper):
        self._shipper = shipper

    @property
    def shipper(self):
        return self._shipper