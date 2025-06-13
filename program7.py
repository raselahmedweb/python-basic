# finding the number of letters, numbers nd words from a sentence

text = input("Write a sentence : ")

numberOfLetters = 0
numberOfNumbers = 0
numberOfWords = 0

for x in text:
    x=x.lower()
    if x >= "a" and x<= "z":
        numberOfLetters = numberOfLetters + 1

    elif x>="0" and x<="9":
        numberOfNumbers = numberOfNumbers + 1

    elif x == " ":
        numberOfWords = numberOfWords + 1


print("Number of letters : ", numberOfLetters)
print("Number of words : ", numberOfWords+1)
print("Number of numbers : ", numberOfNumbers)
