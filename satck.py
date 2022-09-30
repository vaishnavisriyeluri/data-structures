import sys
from array import *
a=array('i',[])
while True:
    print("1.pust 2.pop 3.dispaly 4.exit")
    ch=int(input("enter your choice:"))
    if ch==1:
        ele=int(input("enter the element:"))
        a.append(ele)
        print("inserted")
    elif ch==22:
        if len(a)==0:
            print("stack is empty")
        else:
            print("deleted element is :",pop())
    elif ch==3:
            if len(a)==0:
                print("stack is empty")
            else:
                print("the element in stack is")
                for i in a:
                    print(i)
    elif ch==4:
        sys.exit()
    else:
        print("invalid choice")
