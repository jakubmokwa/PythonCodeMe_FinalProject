from bubble_sort import bubble_sort
from bogo_sort import bogo_sort
from counting_sort import counting_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from quick_sort import quick_sort
from selection_sort import selection_sort


class Sorting_Algorithms:
    def __init__(self):
        self.bogo_times = list()
        self.bubble_times = list()
        self.counting_times = list()
        self.insertion_times = list()
        self.merge_times = list()
        self.quick_times = list()
        self.selection_times = list()

    def show_average_times(self):
        print('\n')
        if len(self.bogo_times) != 0:
            print('BogoSort: ', format(sum(self.bogo_times) / len(self.bogo_times), ".8f"), 's')
        if len(self.bubble_times) != 0:
            print('BubbleSort: ', format(sum(self.bubble_times) / len(self.bubble_times), ".8f"), 's')
        if len(self.counting_times) != 0:
            print('CountingSort: ', format(sum(self.counting_times) / len(self.counting_times), ".8f"), 's')
        if len(self.insertion_times) != 0:
            print('InsertionSort: ', format(sum(self.insertion_times) / len(self.insertion_times), ".8f"), 's')
        if len(self.merge_times) != 0:
            print('MergeSort: ', format(sum(self.merge_times) / len(self.merge_times), ".8f"), 's')
        if len(self.quick_times) != 0:
            print('QuickSort: ', format(sum(self.quick_times) / len(self.quick_times), ".8f"), 's')
        if len(self.selection_times) != 0:
            print('SelectionSort: ', format(sum(self.selection_times) / len(self.selection_times), ".8f"), 's')
        print('\n')

    def sort_list(self, to_sort):
        print('\n')
        if len(to_sort) <= 10:
            sorted_list, timer = bogo_sort(to_sort)
            self.bogo_times.append(timer)
            print(f'BogoSort sorted: {sorted_list} in {format(timer, ".8f")} seconds')
        sorted_list, timer = bubble_sort(to_sort)
        self.bubble_times.append(timer)
        print(f'BubbleSort sorted: {sorted_list} in {format(timer, ".8f")} seconds')
        sorted_list, timer = counting_sort(to_sort)
        self.counting_times.append(timer)
        print(f'CountingSort sorted: {sorted_list} in {format(timer, ".8f")} seconds')
        sorted_list, timer = insertion_sort(to_sort)
        self.insertion_times.append(timer)
        print(f'InsertionSort sorted: {sorted_list} in {format(timer, ".8f")} seconds')
        sorted_list, timer = merge_sort(to_sort)
        self.merge_times.append(timer)
        print(f'MergeSort sorted: {sorted_list} in {format(timer, ".8f")} seconds')
        sorted_list, timer = quick_sort(to_sort)
        self.quick_times.append(timer)
        print(f'QuickSort sorted: {sorted_list} in {format(timer, ".8f")} seconds')
        sorted_list, timer = selection_sort(to_sort)
        self.selection_times.append(timer)
        print(f'SelectionSort sorted: {sorted_list} in {format(timer, ".8f")} seconds')
        print('\n')

    def obj_bogo_sort(self, to_sort):
        to_sort, timer = bogo_sort(to_sort)
        self.bogo_times.append(timer)
        return to_sort, timer

    def obj_bubble_sort(self, to_sort):
        to_sort, timer = bubble_sort(to_sort)
        self.bubble_times.append(timer)
        return to_sort, timer

    def obj_counting_sort(self, to_sort):
        to_sort, timer = counting_sort(to_sort)
        self.counting_times.append(timer)
        return to_sort, timer

    def obj_insertion_sort(self, to_sort):
        to_sort, timer = insertion_sort(to_sort)
        self.insertion_times.append(timer)
        return to_sort, timer

    def obj_merge_sort(self, to_sort):
        to_sort, timer = merge_sort(to_sort)
        self.merge_times.append(timer)
        return to_sort, timer

    def obj_quick_sort(self, to_sort):
        to_sort, timer = quick_sort(to_sort)
        self.quick_times.append(timer)
        return to_sort, timer

    def obj_selection_sort(self, to_sort):
        to_sort, timer = selection_sort(to_sort)
        self.selection_times.append(timer)
        return to_sort, timer
