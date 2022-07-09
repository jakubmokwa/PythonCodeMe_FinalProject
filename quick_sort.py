from time import perf_counter


def quick_sort(to_sort):
    size = len(to_sort)
    if size < 2:
        return to_sort

    index = 0
    for i in range(1, size):
        if to_sort[i] <= to_sort[0]:
            index += 1
            to_sort[i], to_sort[index] = to_sort[index], to_sort[i]

    to_sort[0], to_sort[index] = to_sort[index], to_sort[0]
    left = quick_sort((to_sort[:index]))
    right = quick_sort(to_sort[index + 1:])

    to_sort = left + [to_sort[index]] + right
    return to_sort


def init_quick_sort(to_sort):
    start_timer = perf_counter()
    quick_sort(to_sort)
    end_timer = perf_counter() - start_timer
    return to_sort, end_timer


def main():

    print(init_quick_sort([1, 2, 3, 4, 5, 0, 6, 6, 6, 5]))


if __name__ == '__main__':
    main()
