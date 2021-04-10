from autofactory import AutoFactory

factory = AutoFactory()

for name in 'Ciaz', 'Tesla':
    car = factory.create_instance(name)
    car.start()
    car.stop()