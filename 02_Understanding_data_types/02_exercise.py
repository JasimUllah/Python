# Entring a two digit number so that the output could be added

two_digit_sum = input("Type a two digit number: ")
# print(type(two_digit_sum))
# print(int(two_digit_sum[0]) + int(two_digit_sum[1]))

# OR

# first_digit = int(two_digit_sum[0])
# second_digit = int(two_digit_sum[1])

# result = first_digit + second_digit
# print(result)

# OR

first_digit = two_digit_sum[0]
second_digit = two_digit_sum[1]

result = int(first_digit) + int(second_digit)
print(result)