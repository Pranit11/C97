introString =input("Enter a word or a sentence or a paragraph, your choice and I will try to guess how many words and characters there are :) GO ON : ")
characterCount=0
wordCount=1
for i in introString:
    characterCount=characterCount+1

    if(i==" "):
        wordCount=wordCount+1
print("my guess for number of words isssss : ")
print(wordCount)

print("my guess for number of characters isssss : ")
print(characterCount)

introString =input("Now if you had fun then you can again try to enter a word or a sentence or a paragraph, your choice and I will try to guess how many words and characters there are :) GO ON : ")
characterCount=0
wordCount=1
for i in introString:
    characterCount=characterCount+1

    if(i==" "):
        wordCount=wordCount+1
print("my guess for number of words isssss : ")
print(wordCount)

print("my guess for number of characters isssss : ")
print(characterCount)