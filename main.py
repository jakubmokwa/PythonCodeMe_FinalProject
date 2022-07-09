from main_class import Sorting_Algorithms
from random import randint


def get_length():
    while True:
        try:
            n = int(input("Write length of list (BogoSort won't be executed with n > 10) -> "))
            if n <= 1:
                print("Incorrect, integer must be > 1")
                continue
        except ValueError:
            print("Integer expected")
        else:
            break
    return n


def start_sorting(n, flag, main_object):
    to_sort = list()
    if flag:
        for i in range(n):
            to_sort.append(randint(10, 50))
    else:
        for i in range(n):
            to_sort.append(randint(0, 10))
    print('Generated list: ', to_sort)
    main_object.sort_list(to_sort)


def test_all_algorithms(main_object):
    while True:
        print('Choose range to generate list: ')
        print('[1] <10, 50>')
        print('[2] <0, 10>')
        print('[0] Go back')
        match input():
            case '1':
                n = get_length()
                start_sorting(n, True, main_object)
            case '2':
                n = get_length()
                start_sorting(n, False, main_object)
            case '0':
                break


def print_menu():
    print('[1] Test all algorithms')
    print('[2] Test selected algorithm')
    print('[3] Print average working times of algorithms')
    print('[0] Quit')


def print_algorithm_choice():
    print('[1] BogoSort')
    print('[2] BubbleSort')
    print('[3] CountingSort')
    print('[4] InsertionSort')
    print('[5] MergeSort')
    print('[6] QuickSort')
    print('[7] SelectionSort')
    print('[0] Go back')


def create_list(n, start=0, end=50):
    created_list = list()
    for i in range(n):
        created_list.append(randint(start, end))
    return created_list


def test_selected_algorithm(main_object):
    n = get_length()
    to_sort = create_list(n)
    print('Created list: ', to_sort)
    while True:
        print_algorithm_choice()
        match input():
            case '1':
                if n > 10:
                    print('Too long for bogo sort')
                    continue
                sorted_list, timer = main_object.obj_bogo_sort(to_sort)
                sorting_type = 'BogoSort'
                print(f'{sorting_type} sorted: {sorted_list} in {format(timer, ".8f")}')
                break
            case '2':
                sorted_list, timer = main_object.obj_bubble_sort(to_sort)
                sorting_type = 'BubbleSort'
                print(f'{sorting_type} sorted: {sorted_list} in {format(timer, ".8f")}')
                break
            case '3':
                sorted_list, timer = main_object.obj_counting_sort(to_sort)
                sorting_type = 'CountingSort'
                print(f'{sorting_type} sorted: {sorted_list} in {format(timer, ".8f")}')
                break
            case '4':
                sorted_list, timer = main_object.obj_insertion_sort(to_sort)
                sorting_type = 'InsertionSort'
                print(f'{sorting_type} sorted: {sorted_list} in {format(timer, ".8f")}')
                break
            case '5':
                sorted_list, timer = main_object.obj_merge_sort(to_sort)
                sorting_type = 'mergeSort'
                print(f'{sorting_type} sorted: {sorted_list} in {format(timer, ".8f")}')
                break
            case '6':
                sorted_list, timer = main_object.obj_quick_sort(to_sort)
                sorting_type = 'quickSort'
                print(f'{sorting_type} sorted: {sorted_list} in {format(timer, ".8f")}')
                break
            case '7':
                sorted_list, timer = main_object.obj_selection_sort(to_sort)
                sorting_type = 'selectionSort'
                print(f'{sorting_type} sorted: {sorted_list} in {format(timer, ".8f")}')
                break
            case '0':
                break
            case _:
                continue



def main():
    main_object = Sorting_Algorithms()
    while True:
        print_menu()
        match input():
            case '1':
                test_all_algorithms(main_object)
            case '2':
                test_selected_algorithm(main_object)
            case '3':
                main_object.show_average_times()
            case '0':
                break
            case _:
                continue


if __name__ == '__main__':
    main()
