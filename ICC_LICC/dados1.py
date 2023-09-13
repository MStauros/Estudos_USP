import codecs

entrada_int = int(input())
entrada_hex = "{0:#x}".format(entrada_int)
entrada_byt = bytes.fromhex(entrada_hex[2:])
entrada_crt = codecs.decode(entrada_byt, encoding="UTF-8", errors="replace")

print(entrada_crt)