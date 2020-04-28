import json
from difflib import get_close_matches
dictPath = "data/data.json"
data = json.load(open(dictPath))

def translate(word):
    word = word.lower()
    capWord = word.capitalize()
    if capWord in data:
        return data[capWord]
    elif word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y/N: " % get_close_matches(word, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it"
    
word = input("Enter word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else: 
    print(output)
