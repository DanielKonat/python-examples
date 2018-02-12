def insertionsort(alist):
    for index in range(1,len(alist)):
            currentvalue=alist[index]
            pos=index
    while pos>0 and alist[pos]-1 > currentvalue:
        alist[pos]=alist[pos -1]
        pos=pos-1
        alist[pos]=currentvalue
alist=[70,75,76,98]
insertionsort(alist)
print(alist)

