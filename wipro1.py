str=input("Enter string:")
word= str.split()
n=int(input("enter count:"))
wordl=[]
letters={}
for ch in word:
     if ch in letters:
         letters[ch] +=1
     else:
        letters[ch]=1
        
for key in letters:
    if letters[key]>=n:
        wordl.append(key)
        
if len(wordl)>0:
    print(wordl)
else:
    print("NA")