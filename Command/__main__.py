import sys

from Interfaces.update_order import UpdateOrder
from Interfaces.create_order import CreateOrder
from Interfaces.ship_order import ShipOrder
from Interfaces import NoCommand

def get_commands():
    commands = (CreateOrder, UpdateOrder, ShipOrder)
    if len(sys.argv) < 2:
        print_usage(commands)
        exit()

    return dict([cls.name, cls] for cls in commands)


def print_usage(commands):
    print('Commands to use:')
    for cmd in commands:
        print(f'    {cmd.description}')

def parse_command(commands, args):
    cmd = commands.setdefault(args[0], NoCommand.NoCommand)
    return cmd(args)

if __name__ == '__main__':
    commands = get_commands()
    command = parse_command(commands, sys.argv[1:])
    command.execute()