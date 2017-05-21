# Implementating rsa algorithm
import math

#a = int(raw_input("Enter your msg: "))
p = 101
q = 113
n = p * q
phi_n = (p -1) * (q - 1)
b = 3533
x = 9726
y = 6597

def rsa():
    en = (x ** b) % n
    print 'encrypted msg ...', en
    #y = pow(b, -1) % phi_n
    de = (en ** y) % n
    print 'decrypted msg ...', de

rsa()
