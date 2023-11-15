import random
import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("두 수는 모두 소수여야 합니다.")
    elif p == q:
        raise ValueError("p와 q는 같을 수 없습니다.")

    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randrange(1, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(1, phi)

    d = mod_inverse(e, phi)
    
    return ((e, n), (d, n))

def encrypt(message, public_key):
    e, n = public_key
    cipher = [pow(ord(char), e, n) for char in message]
    return cipher

def decrypt(cipher, private_key):
    d, n = private_key
    plain = [chr(pow(char, d, n)) for char in cipher]
    return ''.join(plain)

# Example:
if __name__ == "__main__":
    p = 61
    q = 53
    public_key, private_key = generate_keypair(p, q)
    message = "This is RSA assignment."
    encrypted_msg = encrypt(message, public_key)
    decrypted_msg = decrypt(encrypted_msg, private_key)
    
    print("원본 메시지:", message)
    print("암호화 메시지:", ''.join(map(str, encrypted_msg)))
    print("복호화 메시지:", decrypted_msg)
