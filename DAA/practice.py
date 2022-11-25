def rec_fib(n):
    if (n <= 1):
        return n
    else:
        return (rec_fib(n-1) + rec_fib(n-2))

nterms = int(input("Number of terms: "))
if(nterms <= 0):
    print("Enter Positive Integer")
else:
    for i in range(nterms):
        print(rec_fib(i))