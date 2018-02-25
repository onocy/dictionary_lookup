import json
from difflib import get_close_matches

d = json.load(open('dictionary.json'))

def translate(word):
    word = word.upper()
    if word in d:
        return d[word]
    elif word.title() in d:
        return d[word.title()]
    elif len(get_close_matches(word, d.keys())) > 0:
        response = input("Did you mean %s instead? Y if yes, N if no: " % get_close_matches(word, d.keys())[0].lower())
        if response.lower() == 'y':
            return d[get_close_matches(word, d.keys())[0]]
        else:
            return 'Try again.'
    else:
        return "This word is not in the dictionary."

word = input("Enter word: ")
output = translate(word)
print(type(output))
if '\n' not in output:
    print(output)
else:
    for line in output:
        print(line)
