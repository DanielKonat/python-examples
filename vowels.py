v=("a","e","i","o","u")
fn=input("enter file name:")
f=open(fn,"r")
r=f.readlines()
i=1
nv=0
for l in r:
        print("line:",l)
        for c in l:
               if c in v:
                     nv+=1
                     print("vowels in line:",nv)
                     i+=1
