import hashlib


# print(int(hashlib.sha256("password".encode()).hexdigest(), 16))
n = 19
print(n)
print(bin(n))
print(oct(n))
enc_n = hex(n)
print(enc_n)
print(int(enc_n, 16))