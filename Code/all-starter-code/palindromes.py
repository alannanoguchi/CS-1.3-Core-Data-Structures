#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


# def is_palindrome(text):
#     """A string of characters is a palindrome if it reads the same forwards and
#     backwards, ignoring punctuation, whitespace, and letter casing."""
#     # implement is_palindrome_iterative and is_palindrome_recursive below, then
#     # change this to call your implementation to verify it passes all tests
#     assert isinstance(text, str), 'input is not a string: {}'.format(text)
#     return is_palindrome_iterative(text)
#     # return is_palindrome_recursive(text)

def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    text = text.rstrip().lower()
    new_text = ""
    
    for character in text:
        if character in string.ascii_letters:
            new_text += character
            
            
    return is_palindrome_iterative(new_text)
    # return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    # TODO: implement the is_palindrome function iteratively here
    pass
    # once implemented, change is_palindrome to call is_palindrome_iterative
    # to verify that your iterative implementation passes all tests
    # compare first and last item in string and iterate through the string
    # check if each char matches, if they don't return false
    # keep doing this until indicies == or pass eachother

    left_index = 0
    right_index = len(text) - 1
    
    while left_index <= right_index:         # the loop stops so the indexes are not overlapping
        if text[left_index] != text[right_index]:
            return False
        left_index += 1
        right_index -= 1
    return True

# print(is_palindrome_iterative("tacocat"))  # True
# print(is_palindrome_iterative("deed"))   #True
# print(is_palindrome_iterative("asdf"))    #False

def is_palindrome_recursive(text, left_index, right_index):
    # TODO: implement the is_palindrome function recursively here
    pass
    # once implemented, change is_palindrome to call is_palindrome_recursive
    # to verify that your iterative implementation passes all tests

    # base cases
    if text[left_index] != text[right_index]:
        return False
    if left_index == right_index or left_index > right_index:  # if the left index is equal to the right idnex or if the left index goes past the right index
        return True
    # recursive case
    return is_palindrome_recursive(text, left_index + 1, right_index - 1)

# test_str = 'deed'  # True
# test_str = 'tacocate'   # False
# print(is_palindrome_recursive(test_str, 0, len(test_str) -1))



def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
