from Crypto.Hash import SHA256
from Crypto.Hash import MD5

data = open('dados.txt').read()

hash = MD5.new(data.encode())
print(hash.hexdigest())