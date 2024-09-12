def FBR (n):
    if n ==0:                           #base case
        print("Complete")
        return 
    if  n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")  
    elif n % 5 == 0:
        print("Buzz")
    elif n % 3 == 0:
        print("Fizz")
    else:
        print(n)
    FBR(n-1)
FBR(100)

    