import codecs

hex = 'HAERAB8BAQAGGgJLU1NQCRgc686974207468652062756c6c277320657965'
b64 = codecs.encode(codecs.decode(hex, 'hex'), 'base64').decode()
print(b64)
