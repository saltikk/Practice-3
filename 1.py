n=int(input())

def valid(n):
    if n==0:
        print("Not valid")
    else:
        res=True
        while n>0:
            digit=n%10
            if digit%2!=0:
                res=False
                break
            n=n//10
        if res:
            print("Valid")
        else:
            print("Not valid")

valid(n)