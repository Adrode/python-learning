double = lambda x: x * 2
print(double(4))

cube = lambda x: x ** 3
print(cube(3))

full_name = lambda first, last: first + ' ' + last
print('Adrian', 'W.')

is_even = lambda x: x % 2 == 0
print(is_even(4))
print(is_even(5))

max_value = lambda x, y: x if x > y else y
print(max_value(2, 5))

min_value = lambda x, y: x if x < y else y
print(min_value(2, 5))

age_check = lambda age: True if age >= 18 else False
print(age_check(18))
print(age_check(32))
print(age_check(11))