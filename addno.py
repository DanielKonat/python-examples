f=open("addno.txt","w")
ch='y'
while ch=='y':
    n=input("enter no:")
    f.write("\n")
    f.write(n)
    ch=input("do want contune")
f.close
