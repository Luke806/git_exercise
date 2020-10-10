def print_fib(n):
    first = 1
    second = 1
    print(first)
    print(second)
    for i in range(n-1):
        third = first + second
        print(third)
        first=second
        second=third
print_fib(10)