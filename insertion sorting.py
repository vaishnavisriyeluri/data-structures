def insertionsort(lst):
    for i in range(1,len(lst)):
        x=lst[i]
        j=i-1
        while j>=0 and x<lst[j]:
            lst[j+1]=lst[j]
            j=j-1
            lst[j+1]=x
    return lst
n=int(input("enter the size of an array:"))
l=[]
for i in range(n):
    ele=int(input("entre the elements:"))
    l.append(ele)
print(insertionsort(l))