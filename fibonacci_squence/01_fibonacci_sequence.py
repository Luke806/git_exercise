# fibonacci 수열 sequence
# 1 1 2 3 5 8 13 21
# 0 1 2 3 4 5 6
# fib(3) = 3
# fib(4) = 5
# fib(5) = 8
# fib(6) = 13

# variable
# 1.global
# 2.local
def print_fib(n):
    first = 1
    second = 1
    print(first)
    print(second)
    for i in range(n - 1):
        third = first + second
        print(third)
        first = second
        second = third
print_fib(5)


'''
fibonacci를 그 수까지 
'''

# fib(5) 1 1 2 3 5 8
# fib(6) 1 1 2 3 5 8 13