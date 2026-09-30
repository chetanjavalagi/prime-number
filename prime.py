print("name")
num=int(input("enter number:"))

if num<=1:
    print("not a prime number")
else:
    for i in range(2,num):
        if num % i ==0:
            print("not a prime nuber")
            break
    else:
        print("prime number")
print("program modified succesfulluy")
