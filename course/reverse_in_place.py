input_string = list("Using a palindrome here would be a bad idea.")
print(input_string)


def rip():
    i = len(input_string)-1
    j = 0
    tmp = 0
    # This can also be done from the end of the array
    while i > j:
        tmp = input_string[j]
        input_string[j] = input_string[i]
        input_string[i] = tmp
        i -= 1
        j += 1
    print(input_string)


rip()
