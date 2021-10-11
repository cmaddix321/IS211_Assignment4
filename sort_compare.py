import argparse
import time
# other imports go here

import random


def get_me_random_list(n):
    """Generate list of n elements in random order
    
    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list
    

def insertion_sort(a_list):
    t0 = time.clock()
    for index in range(1, len(a_list)):

        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1
            a_list[position] = current_value
    t1 = time.clock() - t0
    return t1
    pass


def shell_sort(a_list):
    t0 = time.clock()
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)

        sublist_count = sublist_count // 2
    t1 = time.clock() - t0
    return t1
    pass


def gap_insertion_sort(a_list, start, gap):

    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i
        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap
            a_list[position] = current_value

    pass


def python_sort(a_list):
    t0 = time.clock()
    a_list.sort()
    t1 = time.clock() - t0
    return t1
    pass


if __name__ == "__main__":

    total_record_shell = 0
    total_record_insert = 0
    total_record_python = 0

    n = 100  # number of list
    size = 500  # size of list
    record_shell = 0
    record_insert = 0
    record_python = 0

    for i in range(n):

        x = get_me_random_list(size)

        shell = shell_sort(x)
        insert = insertion_sort(x)
        python = python_sort(x)
        record_shell += shell
        record_insert += insert
        record_python += python



    total_record_shell += record_shell/n
    total_record_insert += record_insert/n
    total_record_python += record_python/n


    size = 1000  # size of list
    record_shell = 0
    record_insert = 0
    record_python = 0

    for i in range(n):

        x = get_me_random_list(size)

        shell = shell_sort(x)
        insert = insertion_sort(x)
        python = python_sort(x)
        record_shell += shell
        record_insert += insert
        record_python += python

    total_record_shell += record_shell / n
    total_record_insert += record_insert / n
    total_record_python += record_python / n

    size = 10000  # size of list
    record_shell = 0
    record_insert = 0
    record_python = 0

    for i in range(n):

        x = get_me_random_list(size)

        shell = shell_sort(x)
        insert = insertion_sort(x)
        python = python_sort(x)
        record_shell += shell
        record_insert += insert
        record_python += python

    total_record_shell += record_shell / n
    total_record_insert += record_insert / n
    total_record_python += record_python / n


    txt = "Shell Sort took {time:.20f} seconds to run, on average"
    print(txt.format(time=total_record_shell / 3, open=size))
    txt = "Insertion Sort took {time:.20f} seconds to run, on average"
    print(txt.format(time=total_record_insert / 3, open=size))
    txt = "Python Sort took {time:.20f} seconds to run, on average"
    print(txt.format(time=total_record_python / 3, open=size))

    """Main entry point"""
    pass
