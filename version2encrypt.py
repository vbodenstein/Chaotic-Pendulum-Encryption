def byteArrayXOR(a, b):
    # Calculate the elementwise XOR and return the result as bytes.
    return bytes([x^y for (x,y) in zip(a,b)])

def encryption(frequency):
    message = bytes(input("What do you want to encrypt?"), 'ascii')
    key = getData(frequency, len(message))
    ciphertext = byteArrayXOR(message, key)
    recovered = byteArrayXOR(ciphertext, key)
    print(f"Message: {message}\nKey: {key}\nCiphertext: {ciphertext}\nrecovered: {recovered}")
