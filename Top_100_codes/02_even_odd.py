'''num=int(input("Enter your number"))
if num%2==0:
    print("Even")
else:
    print("Odd")'''

def isEven(num):
    return not num&1
if __name__=="__main__":
    num=16
    if isEven(num):
        print("Even")
    else:
        print("Odd")