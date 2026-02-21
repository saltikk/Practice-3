n=int(input())

def usual(n):
    if n<=0:
        return False
    
    for i in [2,3,5]:
        while n%i==0:
            n//=i
        
    return n==1

if usual(n):
    print("Yes")
else:
    print("No")