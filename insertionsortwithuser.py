def insertionsort(alist):
    for index in range(1,len(alist)):
            currentvalue=alist[index]
            pos=index
    while pos>0 and alist[pos]-1 > currentvalue:
        alist[pos]=alist[pos -1]
        pos=pos-1
        alist[pos]=currentvalue
alist=list()
num=input("enter no of element in the list")
for i in range (0,int(num)):
    n=input("enter element")
    alist.append(int(n))
insertionsort(alist)
print(alist)
