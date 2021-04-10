from .abs_car import AbsCar

class NullCar(AbsCar):
    def __init__(self, name) -> None:
        super().__init__()
        self._name = name

    def start(self):
        print(f'Null car of name {self._name} started')

    def stop(self):
        print(f'Null car of name {self._name} stopped')