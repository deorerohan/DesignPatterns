from director import Director
from MyBuilder import MyBuilder


builder = Director(MyBuilder())
builder.build_computer()
machine = builder.get_computer()
machine.display()
