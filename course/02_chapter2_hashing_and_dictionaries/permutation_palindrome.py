def permutation_palindrome(instring):
    """
    Friedman's Something Or Other of Palindromes:
    a collection of characters can be arranged (permuted) into a palindrome if
    and only if there is an even number of each character in the collection or
    there is an even number except for one character which only occurs once
    """
    instring = instring.replace(" ","")
    letter_dict = {}
    # Fill our dictionary
    for char in instring:
        if char in letter_dict:
            letter_dict[char] += 1
        else:
            letter_dict[char] = 1

    print(letter_dict)
    return

text = "a man a plan a canal panama"
permutation_palindrome(text)
