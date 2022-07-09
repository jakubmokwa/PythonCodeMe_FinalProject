from values_check import values_check
from time import perf_counter


def positive_check(check_list):
    for i in check_list:
        if i < 0:
            raise ValueError("Takes only positive values, negative(s) were given")


def integer_check(to_sort):
    for value in to_sort:
        if not isinstance(value, int):
            raise ValueError("Takes only integer values, float were given")


def counting_sort(to_sort):
    values_check(to_sort)
    positive_check(to_sort)
    integer_check(to_sort)

    start_timer = perf_counter()
    highest = max(to_sort)
    sorted_list = [0 for _ in range(len(to_sort))]
    count_list = [0 for _ in range(highest + 1)]

    for i in range(len(to_sort)):
        count_list[to_sort[i]] += 1

    for i in range(1, len(count_list)):
        count_list[i] += count_list[i - 1]

    for i in range(len(to_sort)):
        sorted_list[count_list[to_sort[i]] - 1] = to_sort[i]
        count_list[to_sort[i]] -= 1

    end_timer = perf_counter() - start_timer
    return sorted_list, end_timer


def main():
    print(counting_sort([1, 2, 3, 4, 5, 0, 6, 6, 6, 5]))
    print(counting_sort([6, 5, 4, 3, 2, 1, 0]))


if __name__ == '__main__':
    main()
