import re

filename = "C:/Users/anton/Downloads/Рабочий стол/hello.txt"


def get_words(file):
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()
    text = re.sub(r'[^\w\s]', '', text)
    text = text.lower()
    words = text.split()
    words.sort()
    return words


def get_words_dict(words):
    words_dict = dict()

    for w in words:
        if w in words_dict:
            words_dict[w] = words_dict[w] + 1
        else:
            words_dict[w] = 1
    return words_dict


words = get_words(filename)
words_dict = get_words_dict(words)

print("\nWords count:", len(words))
print("\nUni-words count:", len(words_dict))

for word, count in sorted(words_dict.items(), key=lambda x: x[1], reverse=True):
    print(word, count)
