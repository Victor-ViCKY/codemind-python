n=int(input())
e=o=c=0
while n>0:
    k=n%10
    if k%2==0:
        e+=1
    elif k%2!=0:
        o+=1
    n=n//10
    c=c+1
if c==e:
    print("Even")
elif c==o:
    print("Odd")
else:
    print("Mixed")