my_first_variable = 1
my_first_variable = 2

print(type(my_first_variable))

my_first_variable = "Now, I am string!"

print(type(my_first_variable))
print(my_first_variable)

#-----------
# Function
def add_two_numbers(number_one, number_two):
    total = number_one + number_two
    print(total)
#-------------------
def add_two_numbers(number_one, number_two):
    return number_one + number_two
sum_with_return = add_two_numbers(3, 3)
print(sum_with_return)

def square_a_number(number):
    square = number * number
    return
print(square_a_number(5))