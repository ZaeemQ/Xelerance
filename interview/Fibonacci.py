def fib(n):
    a = 0
    b = 1
    sum = 0

    if n == 1:
        print(a)
    else:
        print(a)
        print(b)


        while True:
            c = a + b
            if c > n:
                break
            print(c)
            a = b
            b = c

            if c % 2 != 0:
                sum = sum + c


    print("the sum is :")
    print(sum)


fib(22)
