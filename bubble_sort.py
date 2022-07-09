from time import perf_counter
from values_check import values_check


def bubble_sort(to_sort):
    values_check(to_sort)
    start_timer = perf_counter()
    for i in range(len(to_sort)):
        for j in range(len(to_sort) - i - 1):
            if to_sort[j] > to_sort[j + 1]:
                to_sort[j], to_sort[j + 1] = to_sort[j + 1], to_sort[j]
    end_timer = perf_counter() - start_timer
    return to_sort, end_timer


def main():
    try:
        print(bubble_sort([3, 2, 1, 5, 7, 1, 2, 3, 5, 5]))
    except ValueError as err:
        print('ValueError: ', err)


if __name__ == '__main__':
    main()
