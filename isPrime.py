def isprime(x):
    prime=True
    if x!=0 or x!=1:
        for i in range(2,x):
            if x%i == 0:
                prime=False
                break
    return prime

for j in range(1,1000):
    if isprime(j):
        print(j)
