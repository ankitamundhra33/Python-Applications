import json
import difflib

data = json.load(open("data.json"))

word = input("Enter the word you want to search: ")


def translate(word):
    word = word.lower()
    close = difflib.get_close_matches(word, data.keys())
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(close) > 0:
        print("Did you mean %s instead?" %close[0])
        decide = input("Press y to continue: ")
        if(decide=="y" or decide=="Y"):
            return data[close[0]]
        else:
            return "This word does not exist!"
    else:
        return "This word does not exist!"


output = translate(word)
if type(output) == list:
    for line in output:
        print(line)
else:
    print(output)
