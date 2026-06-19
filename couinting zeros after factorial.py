n = int(input("Enter number: "))

def fac(n):
    if n == 0 or n == 1:
        return 1
    return n * fac(n - 1)

factorial = fac(n)
print("Factorial =", factorial)

f = str(factorial)
zero =0
for i in range(0,len(f)):
    if f[i] == '0':
        zero +=1
print("the number of zeros are :" ,zero)
