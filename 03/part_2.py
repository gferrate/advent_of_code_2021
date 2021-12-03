from bdb import GENERATOR_AND_COROUTINE_FLAGS
from utils import read_csv


class Criterias:
    CO2 = 'CO2'
    O2 = 'O2'


def get_rows_with_num_in_position(data, position, num):
    return list(filter(lambda x: x[int(position)] == num, data))


def get_occurences(data):
    occurences = {}
    row_len = len(data[0])
    for row in data:
        for i in range(row_len):
            occurences.setdefault(i, {}).setdefault(row[i], 0)
            occurences[i][row[i]] += 1
    return occurences


def get_criteria_output(data, criteria):
    rows = data
    occurences = get_occurences(rows)

    for pos in range(len(rows[0])):
        num_occ = occurences[pos]
        if num_occ['0'] == num_occ['1']:
            if criteria == Criterias.O2:
                # Most common
                value = '1'
            elif criteria == Criterias.CO2:
                # Least common
                value = '0'
        else:
            if criteria == Criterias.O2:
                # Most common
                value = '1' if num_occ['1'] > num_occ['0'] else '0'
            elif criteria == Criterias.CO2:
                # Least common
                value = '1' if num_occ['1'] < num_occ['0'] else '0'

        rows = get_rows_with_num_in_position(rows, pos, value)
        occurences = get_occurences(rows)

        if len(rows) == 1:
            break
    assert len(rows) == 1
    return int(rows[0], 2)


def main():
    data = read_csv('03/input.csv')
    data = [x[0] for x in data]

    # Get Oxygen generator rating
    oxygen_generator_rating = get_criteria_output(data, Criterias.O2)

    # Get Oxygen generator rating
    co2_scrubber_rating = get_criteria_output(data, Criterias.CO2)

    print(f'{oxygen_generator_rating = }')
    print(f'{co2_scrubber_rating = }')
    print(f'{oxygen_generator_rating * co2_scrubber_rating = }')


main()
