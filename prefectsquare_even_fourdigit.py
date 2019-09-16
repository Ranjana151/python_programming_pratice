# list of all 4 digit number which is prefect square and even
import math
for i in range(1000,10000):
    n=int(math.sqrt(i))
    if (n*n==i):
        n=i
        while n!=0:
            r=n%10
            n=n//10
            if r%2!=0:
                break
        else:
            print(i)

