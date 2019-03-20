# If we list all the natural numbers below 10 that are multiples of 3 or 5, 
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def problem_1(number):
    var_for_sum = 0
    for num in range(number):
        if num % 3 == 0:
            var_for_sum += num
        elif num % 5 == 0:
            var_for_sum += num
    return var_for_sum
print(problem_1(1000))
