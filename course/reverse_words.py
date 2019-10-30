message = [ 'c', 'a', 'k', 'e', ' ',
            'p', 'o', 'u', 'n', 'd', ' ',
            's', 't', 'e', 'a', 'l' ]

def rip(input_string):
    i = len(input_string)-1
    j = 0
    tmp = 0
    while i > j:
        tmp = input_string[j]
        input_string[j] = input_string[i]
        input_string[i] = tmp
        i -= 1
        j += 1
    return input_string

def reverse_words():
    # Make an list of words not strings
    tmp_str = ''.join(message)
    message1 = tmp_str.split(' ')
    message1 = rip(message1)
    print(message1)

reverse_words()
