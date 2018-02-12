ftr=input("enter file name:")
f1=open(ftr,"r")
rd=f1.read()
ftw=input("enter file name:")
f2=open(ftw,"w")
f2.write(rd)

f1.close()
f2.close()
