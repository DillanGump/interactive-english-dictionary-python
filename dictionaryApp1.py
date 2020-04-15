import json
dictPath = "data/data.json"
data = json.load(open(dictPath))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    else:
        return "The word doesn't exist. Please double check it"
    
word = input("Enter word: ")

print(translate(word))