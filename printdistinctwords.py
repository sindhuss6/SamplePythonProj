#Enter the list of words which can be repititive, out of those print the number of distinct words
#Output should be in the following format
#first line of output is total no of words given
#second line output the number of occurences for each distinct word according to their appearance in the input

num = int(input("Enter the no of words"))
words = []


for i in range(num):
    print("Enter the word")
    str = input()
    words.append(str)

print(words)

distinct_words = []
count = 0
frequency = {}

for eachword in words:
    if eachword in frequency:
        frequency[eachword] +=1
    else:
        frequency[eachword] = 1
        distinct_words.append(eachword)

print("The number of distinct words are:",len(distinct_words))
for key,value in frequency.items():
    print(value, end=' ')