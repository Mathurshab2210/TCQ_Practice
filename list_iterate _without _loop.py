lst=eval(input("enter list"))
s=int(input("enterr start index"))
e=int(input("enter last index"))

def iterate(lst,s,e):
    if s<0 or s>=e:
        return
    print(lst[s])
    iterate(lst,s+1,e)
    
iterate(lst,s,e)