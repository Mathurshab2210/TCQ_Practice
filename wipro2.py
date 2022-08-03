str1=input("Enter test string")
alp=[]
num=[]
for i in str1:
    if i.isalpha():
        alp.append(i)
    else:
        num.append(i)
        
srt=sorted(alp)+sorted(num)
out=''.join(srt)
print(out)