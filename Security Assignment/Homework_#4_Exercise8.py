from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def des_encrypt(key, plaintext):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_plaintext = pad(plaintext.encode(), 8)
    ciphertext = cipher.encrypt(padded_plaintext)
    return ciphertext

def des_decrypt(key, ciphertext):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_text = cipher.decrypt(ciphertext)
    plaintext = unpad(decrypted_text, 8).decode()
    return plaintext

# 키 생성
key = get_random_bytes(8)

# 평문과 키로 암호화하기
plaintext = "Midterm exam starts on Friday"
ciphertext = des_encrypt(key, plaintext)
print("암호화된 결과: ", ciphertext)

# 복호화하기
decrypted_text = des_decrypt(key, ciphertext)
print("복호화된 결과: ", decrypted_text)
