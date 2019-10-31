message = [ 'c', 'a', 'k', 'e', ' ',
            'p', 'o', 'u', 'n', 'd', ' ',
            's', 't', 'e', 'a', 'l' ]

def rip(message, j, i):
    tmp = 0
    while i > j:
        print(i)
        print(j)
        tmp = message[j]
        message[j] = message[i]
        message[i] = tmp
        i -= 1
        j += 1

def reverse_words(message):
    # Step 1: reverse the whole thing by characters
    rip(message, 0, len(message)-1)
    bottom = 0 # beginning of current word. Prime with the beginning of the array.
    # Step2: Loop to find individual words
    for n in range(len(message) + 1):
        if(n == len(message) or message[n] == ' '):
            # Step3: Reverse teh word when we find it
            rip(message, bottom, n-1)
            # reset bottom
            bottom = n + 1
    print(message)
    #message = rip()
    #bottom = 0

reverse_words(message)
