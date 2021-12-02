import csv

"""
down X increases your aim by X units.
up X decreases your aim by X units.
forward X does two things:
It increases your horizontal position by X units.
It increases your depth by your aim multiplied by X.
"""

horiziontal = 0
depth = 0
aim = 0


def operate(command, amount):
    global horiziontal, depth, aim
    if command == 'forward':
        horiziontal += amount
        depth += aim * amount
    elif command == 'down':
        # down increases aim
        aim += amount
    elif command == 'up':
        # up decreases aim
        aim -= amount
    else:
        raise Exception('Invalid command')


def read():
    data = []
    with open('input.csv', 'r') as f:
        reader = csv.reader(f, delimiter=' ')
        for command, amount in reader:
            amount = int(amount)
            data.append((command, amount))
    return data

def main():
    data = read()
    for c, a in data:
        operate(c, a)
    print(f'{horiziontal=}')
    print(f'{depth=}')
    print(f'{horiziontal*depth=}')


main()
