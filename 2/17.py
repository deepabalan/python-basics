

def only_upper(t):
    res = []
    for s in t:
        if s == s.upper():
            res.append(s)
    return res

print only_upper(['a', 'B', 'c']) 
