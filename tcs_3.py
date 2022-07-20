num=int(input("ENter a number"))
#0,0,7,6,14,12,21,18,28 find the 15th term in number series
a=0
b=0
#if odd +7 and for even +6
for i in range(0,num):
     if (i%2 !=0):
         a=a+7
     else:
         b=b+6
        
if (num%2!=0):
    print(num,"term of series is :",a)
else:
    print(num,"term of series is :",b)
 
 