# sorting from longest to shortest


def sort_by_length(words):
    t = []
    for word in words:
        t.append((len(word), word))
    t.sort(reverse=True)

    res = []
    for length, word in t:
        res.append(word)
    return res

print sort_by_length(('largest', 'small', 'encyclopedia'))
