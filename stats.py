def get_num_words(text):
    return len(text.split())


def characters(text):
    chars = {}
    for char in text:
        if char.lower() in chars:
            chars[char.lower()] += 1
        else:
            chars[char.lower()] = 1
    return chars


def sorted_char_list(chars):
    char_list = []
    for char in chars:
        char_list.append({"char": char, "num": chars[char]})
    char_list.sort(reverse=True, key=lambda item: item["num"])
    return char_list
