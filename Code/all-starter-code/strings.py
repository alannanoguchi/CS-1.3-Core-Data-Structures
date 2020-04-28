#!python

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement contains here (iteratively and/or recursively)
    if pattern in text:
        return True
    else:
        return False




def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_index here (iteratively and/or recursively)

    # return find_all_indexes(text, pattern, False)   # from TA during office hours

    if len(pattern) == 0:       # checking to see if there is a given pattern, if not, return 0
        return 0

    for i in range(len(text)):             # for letter in the list text
        for j in range(0, len(pattern)):     # for the letter in the pattern of list pattern
            if pattern[j] != text[i + j]:   # # text[i + j] --> index i increases by the value of j so if j is 0 then i(2) + j(0) = i(2), if j is 1 then i(2) + j(1) = i(3)
                break
            elif j == len(pattern) - 1:      # else of j is equal to the length of the pattern, return the index
                return i
    return None

    """
    bananas
    i = 2 (n)
    j = 0
    loop 1: text (i) range(len(text) - len(pattern)) 0 -> 4
        loop 2: text & pattern(j) range(len(pattern))
            if text[i + j] != pattern[j]:    # text[i + j] --> index i increases by the value of j so if j is 0 then i(2) + j(0) = i(2), if j is 1 then i(2) + j(1) = i(3)
                break           # the break will happen if we do not find a match
            else: 
                return i        # else, we did find the pattern and we return that index
    return None      # the pattern does not exist in the text 
    
    explanaition of loop 2: 
    function text, pattern, index:
        check if pattern is at that index
    """


def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_all_indexes here (iteratively and/or recursively)

    all_indices = []            # create empty list to append all indices that given pattern appears at

    if pattern == "":
        for i in range(len(text)):
            all_indices.append(i)
        return all_indices

    for i in range(len(text) - len(pattern) + 1):             
        for j in range(len(pattern)):    
            if pattern[j] != text[i + j]:   # text[i + j] --> index i increases by the value of j so if j is 0 then i(2) + j(0) = i(2), if j is 1 then i(2) + j(1) = i(3)
                break
        else:           # else, append the index into the list
            all_indices.append(i)
    return all_indices


    # Not passing the test case for an empty string
    # if pattern == '':




""" 
bananas
i = 2 (n)
j = 0
l = list()
find_all_indexes(text, pattern, flag = False)
    loop 1: text (i) range(len(text) - len(pattern)) 0 -> 4
        loop 2: willk compare text & pattern(j) in the range(len(pattern))
            if text[i + j] != pattern[j]:    # text[i + j] --> index i increases by the value of j so if j is 0 then i(2) + j(0) = i(2), if j is 1 then i(2) + j(1) = i(3)
                break           # the break will happen if we do not find a match
            else:   # found an index so continue with the following if statement
                if flag == True:      # 1 index
                    l.append(i)
                    return l
                else:
                    l.append(i)        # else if Flag == False, we did find the pattern and we add that index to a list 
    return l      # the pattern does not exist in the text, l is an empty list 

find_all_indexes('hahahaha', 'ha')    # example of a test
find_index(text, pattern):
    l = find_all_indexes(text, pattern, True)
    if len(l) > 0:      # if length of the list is greater than 0
        return l[0]
    else: # we never found the item
        return None

contains(text, pattern):
    return len(find_index(text, pattern)) != 0   # if find_index returns None then that means the pattern was not found


explanaition of loop 2: 
function text, pattern, index:
    check if pattern is at that index

    true
"""


def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
