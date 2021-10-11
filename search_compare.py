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


def sequential_search(a_list, item):
    t0 = time.clock()
    pos = 0
    found = False
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1

    t1 = time.clock() - t0
    return found, t1
    pass


def ordered_sequential_search(a_list, item):
    t0 = time.clock()
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos + 1
    t1 = time.clock() - t0
    return found, t1


pass


def binary_search_iterative(a_list, item):
    t0 = time.clock()
    first = 0
    last = len(a_list) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    t1 = time.clock() - t0
    return found, t1
    pass
    
    
def binary_search_recursive(a_list, item):
    t0 = time.clock()
    if len(a_list) == 0:
        t1 = time.clock() - t0
        return False, t1
    else:
        midpoint = len(a_list) // 2
    if a_list[midpoint] == item:
        t1 = time.clock() - t0
        return True, t1
    else:
        if item < a_list[midpoint]:
            return binary_search_recursive(a_list[:midpoint], item)
        else:
            return binary_search_recursive(a_list[midpoint + 1:], item)
    pass


def main():
    total_record_seq = 0
    total_record_seq_ord = 0
    total_record_bin_ite = 0
    total_record_bin_rec = 0
    n = 100  # number of list
    size = 500  # size of list
    record_seq = 0
    record_seq_ord = 0
    record_bin_ite = 0
    record_bin_rec = 0
    for i in range (n):

        x = get_me_random_list(size)
        x.sort()
        s = sequential_search(x, -1)
        so = ordered_sequential_search(x, -1)
        record_seq += s[1]
        record_seq_ord += so[1]
        bi = binary_search_iterative(x,-1)
        br = binary_search_recursive(x,-1)
        record_bin_rec += bi[1]
        record_bin_ite += br[1]


    total_record_seq += record_seq/n
    total_record_seq_ord += record_seq_ord/n
    total_record_bin_ite += record_bin_ite/n
    total_record_bin_rec += record_bin_rec/n

    size = 1000  # size of list
    record_seq = 0
    record_seq_ord = 0
    record_bin_ite = 0
    record_bin_rec = 0
    for i in range(n):

        x = get_me_random_list(size)
        x.sort()
        s = sequential_search(x, -1)
        so = ordered_sequential_search(x, -1)
        record_seq += s[1]
        record_seq_ord += so[1]
        bi = binary_search_iterative(x, -1)
        br = binary_search_recursive(x, -1)
        record_bin_rec += bi[1]
        record_bin_ite += br[1]

    total_record_seq += record_seq / n
    total_record_seq_ord += record_seq_ord / n
    total_record_bin_ite += record_bin_ite / n
    total_record_bin_rec += record_bin_rec / n

    size = 10000  # size of list
    record_seq = 0
    record_seq_ord = 0
    record_bin_ite = 0
    record_bin_rec = 0
    for i in range(n):

        x = get_me_random_list(size)
        x.sort()
        s = sequential_search(x, -1)
        so = ordered_sequential_search(x, -1)
        record_seq += s[1]
        record_seq_ord += so[1]
        bi = binary_search_iterative(x, -1)
        br = binary_search_recursive(x, -1)
        record_bin_rec += bi[1]
        record_bin_ite += br[1]

    total_record_seq += record_seq / n
    total_record_seq_ord += record_seq_ord / n
    total_record_bin_ite += record_bin_ite / n
    total_record_bin_rec += record_bin_rec / n


    txt = "Sequential Search took {time:.20f} seconds to run, on average"
    print(txt.format(time=total_record_seq / 3, open=size))
    txt = "Sequential Ordered Search took {time:.20f} seconds to run, on average"
    print(txt.format(time=total_record_seq_ord / 3, open=size))
    txt = "Binary Iterative took {time:.20f} seconds to run, on average"
    print(txt.format(time=total_record_bin_ite / 3, open=size))
    txt = "Binary Recursive took {time:.20f} seconds to run, on average"
    print(txt.format(time=total_record_bin_rec / 3, open=size))

if __name__ == "__main__":
    """Main entry point"""
    main()
    pass
