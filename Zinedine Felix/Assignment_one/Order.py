#Here we get a sentance as input
user_input = str(input("Enter a sentance: "))

#the split function breaks sentance into separate words
words = user_input.split()
#Sort function does the alphabetical sorting
words.sort()

#outputs alphabetical sorted version of sentance
print(words)