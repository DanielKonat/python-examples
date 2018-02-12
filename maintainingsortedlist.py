def findsortedposition(thelist,target):
    low=0
    high=len(thelist)-1
    while low<=high:
         mid=(high+low)/2
    if thelist[mid]==target:
          return mid
    elif target<thelist[mid]:
            high=mid-1
    else:
        low=mid+1
        return low
