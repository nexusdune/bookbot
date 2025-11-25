def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def dict_key(item):
    return item["num"]


def sort_on(text):
    unsorted_list = []
    for ch in text:
        count = text[ch]
        if not ch.isalpha():
            continue
        entry = {"char": ch, "num": count}
        unsorted_list.append(entry)
    unsorted_list.sort(key=dict_key, reverse=True)
    return unsorted_list
