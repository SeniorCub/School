def count_words(sentence):
    words = sentence.split()
    num_words = len(words)
    return num_words


user_input = input("Enter a sentence: ")
result = count_words(user_input)
print(f"The number of words in the sentence is: {result}")
