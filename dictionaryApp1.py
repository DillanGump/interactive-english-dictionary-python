import json
from difflib import get_close_matches
dictPath = "data/data.json"
data = json.load(open(dictPath))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        return "Did you mean %s instead?" % get_close_matches(word, data.keys()) [0]
    else:
        return "The word doesn't exist. Please double check it"
    
word = input("Enter word: ")

print(translate(word))