my_string = "U should always learn coding while doing coding practise"

words =[word.lower() for word in my_string.split()]
words.sort()

print("The sorted words are :")
for word in words:
    print(word)