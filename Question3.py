## Q3 i love codeapp
numberList = list(map(int, input('Enter 12 numbers : ').split()))
wrongGuessList = []
digits = 12
guesses = 5
result = ['_'] * digits

if len(numberList) != 12:
    print('Please enter 12 integers')
else:
    print('_ _ _ _ _ _ _ _ _ _ _ _')
    
    for _ in range(guesses):
        number = int(input('Your guess : '))
        
        if number not in numberList:
            if number not in wrongGuessList:
                wrongGuessList.append(number)
        else:
            index = 0
            
            for _ in range (numberList.count(number)):
                index += numberList[index:].index(number)
                result[index] = numberList[index]
                index += 1

        print(*result, end = ' ')
        print(*wrongGuessList)

    score = 12 - result.count('_')
    
    print(score)
