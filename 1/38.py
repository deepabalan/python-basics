

prefix = "JKLMNOPQ"
suffix = 'ack'
oq = 'uack'

for letter in prefix:
    if letter == 'O' or letter == 'Q':
        print letter + oq
    else:
        print letter + suffix
