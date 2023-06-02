def getData(frequency, size, cutoff = 0.65):
    d.configIO(NumberOfTimersEnabled = 2, FIOAnalog = 4)
    d.configTimerClock(TimerClockBase = 7, TimerClockDivisor = 15)
    trueFrequency = frequency*150
    trueSize = size*8
    direction = 0
    numbers = np.array([])
    while numbers.size < trueSize:
        if direction == 0:
            setFIO(1, 0)
            direction = 1
        elif direction == 1:
            setFIO(0, 1)
            direction = 0
        k = 0
        while k < trueFrequency:
            a1 = d.getAIN(0)
            #a2 = d.getAIN(1)
            #a3 = d.getAIN(2)
            #a4 = d.getAIN(3)
            numbers = np.append(numbers, a1)
            #numbers = np.append(numbers, a2)
            #numbers.append(a3)
            #numbers.append(a4)
            k = k+1
            time.sleep(0.01)
    setFIO(0,0)
    
    #normalization
    minimum = np.amin(numbers)
    numbersFinal = np.subtract(numbers, minimum)
    maximum = np.amax(numbersFinal)
    scaling = 1/maximum
    numbersFinal = np.multiply(numbersFinal, scaling)
    data = np.where(numbers > cutoff, 1, 0)
    
    #output graph
    '''
    dataSize = np.linspace(0, 200, numbers.size)
    plt.plot(dataSize, numbers)
    plt.ylim(0.2,0.8)
    plt.xlabel('Data Number')
    plt.ylabel('Volts')
    '''
    return data


def encrypt(inputMethod = 1, frequency = 0.2):
    # Read in the input file to be encrypted.
    if inputMethod == 0:
        with open('/Users/veronicabodenstein/Classes/input.txt', 'rb') as inputFile:
            rIn1 = inputFile.read()
        rIn = bytes(rIn1, 'utf-8')
    elif inputMethod == 1:
        rIn1 = input("What do you want to encrypt?")
        rIn = bytes(rIn1, 'utf-8')

    # Generate a random key of equal length to the input file.
    key = getData(frequency, len(rIn))

    def byteArrayXOR(a1, a2):
        # Calculate the elementwise XOR and return the result as bytes.
        return bytes(map(lambda x, y: x^y, a1,a2))
            
    
    encrypted = byteArrayXOR(rIn, key)
    print(f'The input is: {rIn} \n')
    print(f'The key is: {bytes(key)} \n')
    print(f'The encrypted data is: {encrypted} \n')
    with open('output.txt', 'wb') as outputFile:
        outputFile.write(encrypted)
    decrypted = byteArrayXOR(encrypted,key).decode('UTF-8')
    print(f'The decrypted data is: {decrypted}')
