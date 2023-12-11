num = int(input("Enter a number"))

if num == 1:
    print(num,"It is not a prime number")
    
elif num>1:
    
    for i in range(2,num):
        if (num % i) == 0:
            print(num,"It is not a prime number")
        break
    else:
        print(num,"It is prime number")
        
