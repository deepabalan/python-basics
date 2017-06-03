# program that sorts words by length with words with same length appear
# in random order.

import random


def unstable_sort(words):
    t = []
    for word in words:
        t.append((len(word), random.random(), word))

    t.sort(reverse=True)

    res = []
    for length, _, word in t:
        res.append(word)
    return res

print unstable_sort(['abc', 'def', 'grapes', 'ghi', 'abcde'])
