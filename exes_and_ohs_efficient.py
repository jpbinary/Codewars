def xo(input_string):
    input_string = input_string.lower()
    return input_string.count('x') == input_string.count('o')

print xo("ooxx")
print xo("xooxx")
print xo("ooxXm")
print xo("zpzpzpp")
print xo("zzoo")
