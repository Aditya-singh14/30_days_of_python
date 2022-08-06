
def fibonacci(n):
    if n<=1:
        return n
    else:
        return (fibonacci(n-1)+fibonacci(n-2))
nterms=10
if nterms<=0:
    print("Please enter positive no.")
else:
    print("Fibonacci seq :")
    for i in range(nterms):
        print(fibonacci(i))