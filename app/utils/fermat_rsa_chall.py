from Crypto.Util.number import *
from sympy import *

def generate_key():
    p = getPrime(1024)
    q = nextprime(p)
    n = p*q
    e = 65537

    return n, e

def encrypt_flag(FLAG: str):
    n, e = generate_key()
    flag = FLAG
    flag = bytes_to_long(flag.encode())
    encrypted_flag = pow(flag, e, n)
    return encrypted_flag,n
