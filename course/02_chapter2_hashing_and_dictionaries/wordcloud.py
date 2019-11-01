from string import punctuation

def wordcloud(text):
    # Normalize our text for the dictionary. Each of these operations is either O(1) or O(n)
    text = text.lower()
    text = text.replace("-", " ")
    table = text.maketrans({key: None for key in punctuation})
    text = text.translate(table)
    print(text)

text = 'After beating the eggs, Dana read the next step-Add milk and eggs, then add flour and sugar.'
wordcloud(text)
