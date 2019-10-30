my_list     = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]

def merge_lists(list_a, list_b):
    list_a.extend(list_b)
    list_a.sort()
    print(list_a)
    return

merge_lists(my_list, alices_list)
