import json
dictPath = "data/data.json"
data = json.load(open(dictPath))

def translate(word):
    return data[word]
    
word = input("Enter word: ")

print(translate(word))