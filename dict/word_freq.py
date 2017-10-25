

def word_frequency(word):
    frequency = {}

    for w in word:
        frequency[w] = frequency.get(w, 0) + 1
    return frequency

print word_frequency(['a', 'b', 'a', 'c'])
