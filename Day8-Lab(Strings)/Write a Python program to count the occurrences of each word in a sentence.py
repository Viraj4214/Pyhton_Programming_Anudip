#take input from the user

sentence = input("Enter a sentence: ")

#convert the sentence to lowercase for uniform counting
sentence = sentence.lower()

#split the sentence into words
words = sentence.split()

#create empty dictionary to store word counts
word_count = {}

#count the occurrences of each word
for word in words:
    if word in word_count:
        word_count[word] = word_count[word] + 1
    else:
        word_count[word] = 1

#display the word counts
print("\n The number of word occurrences: ")
for word,count in word_count.items():
    print(f"{word}: {count}")
