

def make_account():
    return {'balance': 0}


def deposit(account, amount):
    account['balance'] += amount
    return account['balance']


def withdraw(account, amount):
    account['balance'] -= amount
    return account['balance']

user = make_account()
print deposit(user, 20000)
print withdraw(user, 345)
