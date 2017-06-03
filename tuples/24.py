# sort by word length


def my_sort(t):
    res1 = []
    for i in t:
        res1.append((len(i), i))
    res1.sort()

    res2 = []
    for length, i in res1:
        res2.append(i)
    return res2

print my_sort(['alphabetical', 'ghi', 'wordsss', 'abc', 'a', 'def'])
