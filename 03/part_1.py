from bdb import GENERATOR_AND_COROUTINE_FLAGS
from utils import read_csv


def main():
    # I only want to iterate the list once
    data = read_csv('03/input.csv')
    data = [x[0] for x in data]
    gamma_rate_occurrances = {}
    row_len = len(data[0])
    for row in data:
        for i in range(row_len):
            gamma_rate_occurrances.setdefault(i, {}).setdefault(row[i], 0)
            gamma_rate_occurrances[i][row[i]] += 1

    gamma_rate_bin = [None]*row_len
    for i, gamma_rate_occurrances in gamma_rate_occurrances.items():
        gamma_rate_bin[i] = '1' if gamma_rate_occurrances['1'] > gamma_rate_occurrances['0'] else '0'

    epsilon_rate_bin = ['1' if x == '0' else '0' for x in gamma_rate_bin]

    gamma_rate_bin = ''.join(gamma_rate_bin)
    epsilon_rate_bin = ''.join(epsilon_rate_bin)

    print(f'{gamma_rate_bin=}')
    print(f'{epsilon_rate_bin=}')

    gamma_rate_int = int(gamma_rate_bin, 2)
    epsilon_rate_int = int(epsilon_rate_bin, 2)

    print(f'{gamma_rate_int=}')
    print(f'{epsilon_rate_int=}')

    print(f'{gamma_rate_int*epsilon_rate_int=}')


main()
