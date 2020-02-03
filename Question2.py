## Q2
def isPrime(number):
    limit = (number // 2) + 1

    for i in range (2, limit):
        if number % i == 0:
            return False

    return True

def isFloatingPrime(number):
    for i in range(1, 4):
        currentNumber = int(number * (10**i))
        
        if isPrime(currentNumber):
            return True

    return False

number = float(input('Enter a decimal number : '))

while number != 0.0:
    strNumber = str(number)
    
    if len(strNumber) > 13:
        print('Enter no more than 11 decimal places')
    elif number < 1.0 or number > 10.0:
        print('Enter number between 1.0 - 10.0')
    else:
        print(isFloatingPrime(number))
        
    number = float(input('Enter a decimal number : '))
