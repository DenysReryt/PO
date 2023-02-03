import string


def unique_letter(text: str) -> str:
    s = text.translate(str.maketrans('', '',
                                     string.punctuation))
    # https://www.techiedelight.com/ru/remove-punctuations-string-python/

    ls = []
    for i in s.split():
        c = 0
        if i.count(i[c]) != 1:
            while i.count(i[c]) != 1:
                c += 1
            else:
                ls.append(i[c])
        else:
            ls.append(i[c])

    for i in ls:
        if ls.count(i) != 1:
            continue
        else:
            return f'Unique letter: {i}'


if __name__ == '__main__':
    print("Enter/Paste your content. Double Enter to finish.\n")
    print(unique_letter("\n".join(iter(input, ""))))
