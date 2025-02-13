

n=int(input("Number of roes required for triangle="))

for i in range (n,0,-1):
    print((n-i)* " "+i * "*")


for i in range (0,n+1):
    print((n-i)* " "+i * "*")