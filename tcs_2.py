#Write a code to check whether a number is prime or not. use a function check() to check if no is pos or neg. 
#if neg return a msg if pos pass no as parameter to a prime and check whether no is prime or not

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
