from string import punctuation

def wordcloud(text):
    # Normalize our text for the dictionary. Each of these operations is either O(1) or O(n)
    text = text.lower()
    text = text.replace("-", " ")
    table = text.maketrans({key: None for key in punctuation})
    text = text.translate(table)
    word_list = text.split(" ")
    cloud = {word:1 for word in set(word_list)}
    print(cloud)
    for i in word_list:
        cloud[i] += 1
    return cloud

text = 'After beating the eggs, Dana read the next step-Add milk and eggs, then add flour and sugar.'
print(wordcloud(text))
