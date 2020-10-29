def factorial(num):
    result = 1
    for i in range(0, num):

        result *= num - i
    return result
print(factorial(5))


def recursive_factorial(num):
    if num == 1:
        return 1
        
    return num * recursive_factorial(num-1)

print(recursive_factorial(5))