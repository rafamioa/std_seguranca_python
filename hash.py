import hashlib

mensagem = 'Fatec'

h = hashlib.sha1()
h.update(b"\n Um texto que nao pode ser modificado")
print("hashcode sha1: \n" + h.hexdigest())
print('Número de caracteres: ' + str(len(h.hexdigest())))
print('Número de bits: '+ str(h.digest_size * 8))
print('Tamanho em bytes: ' + str(h.digest_size) + "\n")


h = hashlib.sha224()
h.update(b"\n Um texto que nao pode ser modificado")
print("hashcode sha224: \n" + h.hexdigest())
print('Número de caracteres: ' + str(len(h.hexdigest())))
print('Número de bits: '+ str(h.digest_size * 8))
print('Tamanho em bytes: ' + str(h.digest_size) + "\n")

h = hashlib.sha256()
h.update(mensagem.encode('UTF-8'))
print("hashcode sha256: \n" + h.hexdigest())
print('Número de caracteres: ' + str(len(h.hexdigest())))
print('Número de bits: '+ str(h.digest_size * 8))
print('Tamanho em bytes: ' + str(h.digest_size) + "\n")

h = hashlib.sha384()
h.update(b"\n Um texto que nao pode ser modificado")
print("hashcode sha384: \n" + h.hexdigest())
print('Número de caracteres: ' + str(len(h.hexdigest())))
print('Número de bits: '+ str(h.digest_size * 8))
print('Tamanho em bytes: ' + str(h.digest_size) + "\n")

h = hashlib.sha512()
h.update(b"\n Um texto que nao pode ser modificado")
print("hashcode sha512: \n" + h.hexdigest())
print('Número de caracteres: ' + str(len(h.hexdigest())))
print('Número de bits: '+ str(h.digest_size * 8))
print('Tamanho em bytes: ' + str(h.digest_size) + "\n")

h = hashlib.md5()
h.update(b"\n Um texto que nao pode ser modificado")
print("hashcode md5: \n" + h.hexdigest())
print('Número de caracteres: ' + str(len(h.hexdigest())))
print('Número de bits: '+ str(h.digest_size * 8))
print('Tamanho em bytes: ' + str(h.digest_size) + "\n")

h = hashlib.sha3_224()
h.update(b"\n Um texto que nao pode ser modificado")
print("hashcode sha3-224: \n" + h.hexdigest())
print('Número de caracteres: ' + str(len(h.hexdigest())))
print('Número de bits: '+ str(h.digest_size * 8))
print('Tamanho em bytes: ' + str(h.digest_size) + "\n")
