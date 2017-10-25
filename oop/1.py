
balance = 0


def deposit(amount):
    global balance
    balance += amount
    print 'deposited... ', amount
    return 'new balance = %d' % balance


def withdraw(amount):
    global balance
    balance -= amount
    print 'withdrawn... ', amount
    return 'new balance = %d' % balance

print deposit(1000)
print withdraw(200)
