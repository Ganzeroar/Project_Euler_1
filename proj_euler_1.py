def problem_1(number):
    var_for_sum = 0
    for num in range(number):
        if num % 3 == 0:
            var_for_sum += num
        elif num % 5 == 0:
            var_for_sum += num
    return var_for_sum
print(problem_1(1000))
