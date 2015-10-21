def multiples(x):
    if x % 49 == 0 and x % 3 == 0:
        return 'Fang'
    elif x % 7 == 0:
        return 'Fizz'
    elif x % 15 == 0:
        return 'Foo'
    else:
        return 'Far'

# Test.assert_equals(multiples(49), "Fizz")
# Test.assert_equals(multiples(147), "Fang")
# Test.assert_equals(multiples(30), "Foo")
# Test.assert_equals(multiples(51), "Far")
