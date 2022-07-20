s=input("Enter string")
a=0
b=0

for i in s:
    if(i=="*"):
        a=a+1
    elif(i=="#"):
        b=b+1
        
print(a-b)