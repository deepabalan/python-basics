
def store_word(filename):
    t = {}
    new_t = {}
    count = 1
    f = open(filename)
    for line in f:
        s = line.split()
        for ch in s:
            if ch not in t:
                t[ch] = count
            else:
                t[ch] += 1
    for keys, values in sorted(t.items()):
        print (keys, values)

def print_top(filename):
    store_word(filename)

print_top('words.txt')
