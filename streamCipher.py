import random

# Read in the input file to be encrypted.
with open('./input.txt', 'rb') as inputFile:
    rIn = inputFile.read()

# Generate a random key of equal length to the input file.
key = random.sample(range(0,255), len(rIn))

# Define a robust function to calculate the elementwise XOR of two sets of bytes.
def byteArrayXOR(a1, a2):

    # Instantiate two bytearrays.
    arr1 = bytearray()
    arr2 = bytearray()

    # Concatenate these bytearrays with our input bytes.
    arr1.extend(a1)
    arr2.extend(a2)

    # Determine which is the longer of the two arrays, if used generally, and extend the shorter array to match.
    diff = max(len(a1),len(a2))-min(len(a1),len(a2))
    if diff+len(arr1) == len(arr2):
        arr1.extend(bytes(bytearray(diff)))
    else:
        arr2.extend(bytes(bytearray(diff)))
    
    # Calculate the elementwise XOR and return the result as bytes.
    return bytes(map(lambda x, y: x^y, arr1,arr2))

fx = byteArrayXOR(rIn,key)
print(f'The input is: {rIn} \n')
print(f'The key is: {bytes(key)} \n')
print(f'The encrypted data is: {fx} \n')
with open('output.txt', 'wb') as outputFile:
    outputFile.write(fx)
decrypted = byteArrayXOR(fx,key).decode('UTF-8')
print(f'The decrypted data is: {decrypted}')
