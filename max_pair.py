def mx_pr(arr):
    if len(arr)<2:
        print("no such pair")
        return
    a=arr[0]
    b=arr[1]
    c=a*b
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if (arr[i]*arr[j]>c):
                a=arr[i]
                b=arr[j]
                
    return a,b

arr=eval(input('enter array'))
print('max pair is :', mx_pr(arr))