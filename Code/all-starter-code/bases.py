#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # TODO: Decode digits from binary (base 2)
    # ...
    # TODO: Decode digits from hexadecimal (base 16)
    # ...
    # TODO: Decode digits from any base (2 up to 36)
    # ...

    base10_num = 0
    digits = digits[::-1]   # reverses the index order so read from right to left instead of left to right

    for i in range(len(digits)):    # get each digit
        digit = int(digits[i], base=base)   # each individual digit as a number
        base10_num += digit * base ** i     # ex: 1011 = (1*2^3) + (1*2^1) + (1*2^0) binary --> dec
    return base10_num

def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)
    # TODO: Encode number in binary (base 2)
    # ...
    # TODO: Encode number in hexadecimal (base 16)
    # divide number by 16, keep remainder
    # continue dividing by 16 until there 
    # TODO: Encode number in any base (2 up to 36)

    # decimal to hex: 75. 75/16 (division) = 4 (remainder = 11). 4/16 = 0 (remainder 4) --> 11, 4 --> 4B
    # string.digits is '0123456789'
    # string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
    # base_digits = (string.digits + string.ascii_uppercase) # <-- this handles all bases even those with letters
    # string.printable() String of ASCII characters which are considered printable. This is a combination of digits, ascii_letters, punctuation, and whitespace.
    # https://docs.python.org/3/library/string.html


    encoded_num = ""

    while number > 0:   # while the number is greater than 0
        # number = number // base   # divide the number by the base. // returns a integer / returns a float
        # remainder = number % base   # % returns the modulous which is the remainder
        number, remainder = divmod(number, base)

        if remainder >= 10:     # if the remainder is greater than or equal to 10
            encoded_num += string.printable[remainder]   # convert the remainder to its associated number
        else:
            encoded_num += str(remainder) # else it is just the number of the remainder

    return encoded_num[::-1]    # returns the reverse order


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    # TODO: Convert digits from base 2 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from base 2 to base 10 (and vice versa)
    # ...
    # TODO: Convert digits from base 10 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from any base to any base (2 up to 36)
    # ...
    base10 = decode(digits, base1)
    result = encode(base10, base2)
    return result

def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')

# print(decode('1011', 2)) # (1*2^3) + (1*2^1) + (1*2^0) = 11
# print(decode('3D', 16)) # (13*16^0) + (3*16^1) = 61

if __name__ == '__main__':
    main()
