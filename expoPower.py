def calcPower(num,n):
    if(n==1):
        return num
    
    if(n%2):
        return num*calcPower(num,n//2)*calcPower(num,n//2)
    else:
        return calcPower(num,n//2)*calcPower(num,n//2)

a=int(input('Enter number '))
n=int(input('Enter power '))
c=calcPower(a,n)
print(c)