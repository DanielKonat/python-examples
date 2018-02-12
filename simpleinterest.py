f1=open("amt.txt","r")
f2=open("simpleinterest.txt","w")
r=f1.readlines()
l=len(r)
for i in range(l):
    m=float(r.split())
    i=m[0]*m[1]*m[2]/100
    f2.write(m[i]+"  "+str(i))
f1.close()
f2.close()
