while True:
    n1 = int(input('What is the number you want to check if it is prime or not: '))
    for i in range(2,n1+1):
        if n1%i!=0:
            print(f'{n1} is a prime number!')
            break
        else:
            print(f'{n1} is not a prime number! ')
            break