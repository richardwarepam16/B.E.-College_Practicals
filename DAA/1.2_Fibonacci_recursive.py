def rec_fib(n):
    if (n <= 1):
        return n
    else:
        return (rec_fib(n-1)+ rec_fib(n-2))

nterms = int(input("How many terms?: "))
if(nterms <= 0):
    print("Enter a positive integer.")
else:
    print("Fibonacci Sequence:")
    for i in range(nterms):
        print(rec_fib(i))