def prime(n):
    c=0
    for i in range(1,n+1):
        if(n%i == 0):
            c=c+1
    if(c==2):
        print(n," is prime number")
    else:
        print(n,"Not prime")
        
def check(n):
    if(n<0):
        print("enter positive int")
    else:
        prime(n)
        
num=int(input("enter a number"))
check(num)