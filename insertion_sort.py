from values_check import values_check
from time import perf_counter


def insertion_sort(to_sort):
    values_check(to_sort)
    start_timer = perf_counter()

    for i in range(len(to_sort) + 1):
        for j in range(1, i):
            if to_sort[i - j] < to_sort[i - j - 1]:
                to_sort[i - j], to_sort[i - j - 1] = to_sort[i - j - 1], to_sort[i - j]

    end_timer = perf_counter() - start_timer
    return to_sort, end_timer


def main():
    print(insertion_sort([1, 2, 3, 4, 5, 0, 6, 6, 6, 5]))


if __name__ == '__main__':
    main()
