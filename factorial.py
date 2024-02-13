def fact(n):
    if n==1:
        return 1
    f=n*fact(n-1)
    return f
m = int(input("Enter a number : "))
result = fact(m)
print("Factorial of ",m," is ",result)
# End of program