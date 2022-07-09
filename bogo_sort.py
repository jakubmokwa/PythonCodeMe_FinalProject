from values_check import values_check
from random import shuffle
from time import perf_counter


def check_sorting(to_check):
    for i in range(len(to_check) - 1):
        if to_check[i] > to_check[i + 1]:
            return False
    return True


def bogo_sort(to_sort):
    values_check(to_sort)

    start_timer = perf_counter()
    while True:
        shuffle(to_sort)
        if check_sorting(to_sort):
            break

    end_timer = perf_counter() - start_timer
    return to_sort, end_timer


def main():
    try:
        print(bogo_sort([3, 2, 1, 6, 7, 8, 4, 2, 34, 6, 7]), 's')
    except ValueError as err:
        print('ValueError: ', err)


if __name__ == '__main__':
    main()
