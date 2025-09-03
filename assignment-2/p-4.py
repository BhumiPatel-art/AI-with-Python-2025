def my_split(sentence, separator):
    items = []
    word = ""
    for char in sentence:
        if char == separator:
            items.append(word)
            word = ""
        else:
            word += char
    items.append(word)
    return items


def my_join(items, separator):
    result = ""
    for i in range(len(items)):
        result += items[i]
        if i < len(items) - 1:
            result += separator
    return result


def main():
    sentence = input("Please enter sentence:")
    words = my_split(sentence, " ")
    joined = my_join(words, ",")
    print(joined)
    for word in words:
        print(word)


if __name__ == "__main__":
    main()
