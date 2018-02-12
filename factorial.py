fn=open("factorial.txt","w")
def fac(f):
    f=1
    for i in range(1,n+1):
            f=f*i
            i+=1
            print(f)

n=int(input('enter no'))
w=fac(n)
fn.write(str(w))
            
