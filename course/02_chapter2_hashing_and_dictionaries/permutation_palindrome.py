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

    # Check that our dictionary has the right number of the right letters
    unique_chars = 0
    for i in letter_dict:
        if letter_dict[i] % 2 == 0:
            pass
        elif letter_dict[i] > 1: # The string is assymetrical
            return False
        else: # i == 1
            if unique_chars > 1:
                return False
            else:
                unique_chars += 1
    return True

pass_text = "a man a plan a canal panama"
fail_text = "adam aint madam"
print(permutation_palindrome(pass_text))
