from values_check import values_check
from time import perf_counter


def merge_sort(to_sort):
    values_check(to_sort)

    start_timer = perf_counter()
    sort(to_sort)
    end_timer = perf_counter() - start_timer

    return to_sort, end_timer


def sort(to_sort):
    if len(to_sort) > 1:
        half = len(to_sort) // 2
        left = to_sort[:half]
        right = to_sort[half:]

        sort(left)
        sort(right)

        left_ind, right_ind, sorted_ind = 0, 0, 0

        while left_ind < len(left) and right_ind < len(right):
            if left[left_ind] < right[right_ind]:
                to_sort[sorted_ind] = left[left_ind]
                left_ind += 1
            else:
                to_sort[sorted_ind] = right[right_ind]
                right_ind += 1
            sorted_ind += 1

        while left_ind < len(left):
            to_sort[sorted_ind] = left[left_ind]
            left_ind += 1
            sorted_ind += 1

        while right_ind < len(right):
            to_sort[sorted_ind] = right[right_ind]
            right_ind += 1
            sorted_ind += 1

    return to_sort


def main():
    print(merge_sort([1, 2, 3, 4, 5, 0, 6, 6, 6, 2]))


if __name__ == '__main__':
    main()
