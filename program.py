
from tests.car import Car
def main():
    print("hello, world")
    data_type = Car
    rows_len = 5
    cols_len = 5

    #sequence2d = [[data_type() for _ in range(cols_len)] for _ in range(rows_len)]
    r#eturn Array2D(starting_sequence = sequence2d, data_type = data_type)

    #sequence2d [data_type() * cols_len] * rows_len

    sequence2d = []
    for row_index in range(rows_len):
        sequence2d.append([])
        for col_index in range (cols_len):
            sequence2d[row_index].append(data_type())
    return Array2D(starting_sequence = sequence2d, data_type = data_type)

if __name__ == '__main__':
    main()
