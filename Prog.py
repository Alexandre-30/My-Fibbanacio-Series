def fibonacci(n):
    Array=[]
    a,b=0,1
    for _ in range(n):
        Array.append(a)
        a,b=b,a+b
    return Array
n=int(input("Enter the number of times: "))
print(fibonacci(n))