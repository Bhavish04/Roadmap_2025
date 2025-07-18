n=int(input("Enter a number"))
sum=0
for i in range(1,n):
    if n%i==0:
        print(i,end="  ")
        sum=sum+i
if sum==n:
    print("Perfect number")
else:
    print("Not a Perfect number")