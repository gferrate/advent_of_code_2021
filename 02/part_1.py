import csv

horiziontal = 0
depth = 0


def operate(command, amount):
    global horiziontal, depth
    if command == 'forward':
        horiziontal += amount
    elif command == 'down':
        # down adds to depth
        depth += amount
    elif command == 'up':
        # up removes to depth
        depth -= amount
    else:
        raise Exception('Invalid command')


with open('input.csv', 'r') as f:
    reader = csv.reader(f, delimiter=' ')
    for command, amount in reader:
        amount = int(amount)
        operate(command, amount)

print(f'{horiziontal=}')
print(f'{depth=}')
print(f'{horiziontal*depth=}')
