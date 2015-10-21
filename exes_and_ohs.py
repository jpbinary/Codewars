'''Check to see if a string has the same amount of 'x's and 'o's.
The method must return a boolean and be case insensitive.
The string can contains any char.

'''

def xo(input_string):
    string_as_list = list(input_string)
    x_count = 0
    o_count = 0
    for character in string_as_list:
        if character.lower() == 'x':
            x_count += 1
        elif character.lower() == 'o':
            o_count += 1
        else:
            pass
    if x_count == o_count:
        return True
    else:
        return False

print xo("ooxx")
print xo("xooxx")
print xo("ooxXm")
print xo("zpzpzpp")
print xo("zzoo")
