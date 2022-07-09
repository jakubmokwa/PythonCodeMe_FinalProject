from values_check import values_check
from time import perf_counter


def selection_sort(to_sort):
    values_check(to_sort)
    start_timer = perf_counter()

    for i in range(0, len(to_sort)):
        min_value = to_sort[i]
        index = i
        for j in range(i + 1, len(to_sort)):
            if to_sort[j] < min_value:
                min_value = to_sort[j]
                index = j

        to_sort[i], to_sort[index] = min_value, to_sort[i]

    end_timer = perf_counter() - start_timer
    return to_sort, end_timer


def main():
    print(selection_sort([1, 2, 3, 4, 5, 0, 6, 6, 6, 2]))


if __name__ == '__main__':
    main()
