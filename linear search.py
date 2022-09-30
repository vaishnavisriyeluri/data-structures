print("Binary search")
print("1.recusive method")
print("2.non-recursive method")
y=int(input("enter your choice of method for searching:"))
if y==1:
    def binarysearch(l,low,high,key):
        if low<=high:
            mid=(low+high)//2
        if l[mid]==key:
            return mid
        elif l[mid]>key:
            return binarysearch(l,low,mid-1,key)
        else:
            return binarysearch(l,mid+1,high,key)
    return -1
else:
    def binarysearch(l,low,high,key):
        while low<=high:
            mid=(low+high)//2
            if l[mid]==key:
                return mid
            elif l[mid]>key:
                high=mid-1
            else:
                low=mid+1
         return -1
l=[]
n=int(input("enter no.of elements:"))
low=0
high=n-1
for i in range(n):
    ele=int(input("enter the elements:"))
    l.append(ele)
key=int(input("enter the elements to be found:"))
result=binarysearch(l,low,high,key)
if result==1:
    print("element not found")
else:
    print("element found at index:",result)
        
    
        