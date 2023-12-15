def factor(x):
    print("The factor of ",x, "are ")
    for i in range(1,x+1):
        if x % i == 0:
            print(i)
            
num = 320
factor(num)