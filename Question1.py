## Q1
def lengthAlphabeticalOrder(str):
    return -len(str), str.lower()

def acronym(inputWords):
    acronym = ''
    
    for word in (inputWords):
        if word[0].isupper():
            acronym += word[0]
            
    return acronym
    
acronymList = []
numberOfWords = int(input())

for i in range (numberOfWords):
    inputWords = list(input().split())
    
    acronymList.append(acronym(inputWords))
    
acronymList.sort(key = lengthAlphabeticalOrder)

for acronym in acronymList:
    print(acronym)
