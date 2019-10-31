list_a = [3, 4, 6, 10, 11, 15]
list_b = [1, 5, 8, 12, 14, 19]

def merge_lists(list_a, list_b):
    result = []
    for i in range(len(list_a)):
        result.append(min(list_a[i], list_b[i]))
        result.append(max(list_a[i], list_b[i]))
    if len(list_b) > len(list_a):
        result.extend(list_b[len(list_a):])
    print(result)

merge_lists(list_a, list_b)
