

def only_upper(t):
    res = []
    for s in t:
        if s.isupper():
            res.append(s)
    return res

print only_upper(['a', 'b', 'C', 'D', 'E'])
