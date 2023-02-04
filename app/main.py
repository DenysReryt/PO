import string


def unique_letter(text: str) -> str:
    s = text.translate(str.maketrans('', '',
                                     string.punctuation))
    # https://www.techiedelight.com/ru/remove-punctuations-string-python/

    ls = []
    for i in s.split():
        for j in i:
            if i.count(j) == 1:
                ls.append(j)
                break
            else:
                continue

    for i in ls:
        if ls.count(i) == 1:
            return f'Unique letter: {i}'
        else:
            continue

if __name__ == '__main__':
    result = unique_letter(input("Enter a text: "))
    if result is not None:
        print(f"The first unique letter: {result}")
    else:
        print("No unique letter was found")
