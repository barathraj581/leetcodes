def prime_no(a):
    for i in range(2,a):
        if(a%i==0):
            print("not prime")
            break
        else:
            print("prime")
            break
num=int(input("enter the number:"))
prime_no(num)
