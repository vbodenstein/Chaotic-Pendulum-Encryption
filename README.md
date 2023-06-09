# Chaotic-Pendulum-Encrytion
This is the project page for our Chatoic Pendulum Encrytion system. A driven double pendulum is by nature a chaotic system, meaning it is highly dependent on, and sensitive to initial conditions. The idea behind this project is to utilize this chaos to produce highly variable keys and encrypt data via symmetric stream cypher. We design a pendulum using aluminum, and to detect its motion, we use neodymium magnets and hall effect sensors. To encrypt a message, we collect a series of bytes from the pendulum and use this as our key. 
Since we can collect data very quickly, an encryption of this sort is theoretically very secure where we can make the key the same length as the message. 


<img width="448" alt="Screen Shot 2023-06-01 at 3 34 16 PM" src="https://github.com/vbodenstein/Chaotic-Pendulum-Encrytion/assets/133536500/81fcaa43-f65b-420c-b719-8bccc97bdfee">


# Table of contents
- [Budget](https://github.com/vbodenstein/Chaotic-Pendulum-Encrytion/blob/main/README.md#budget)
- [Circuits](https://github.com/vbodenstein/Chaotic-Pendulum-Encrytion/blob/main/README.md#circuits)
    - [Motor](https://github.com/vbodenstein/Chaotic-Pendulum-Encrytion/blob/main/README.md#motor-circuit)
    - [Sensor](https://github.com/vbodenstein/Chaotic-Pendulum-Encrytion/blob/main/README.md#sensor-circuit)
    - [Op-amp](https://github.com/vbodenstein/Chaotic-Pendulum-Encrytion/blob/main/README.md#op-amp-circuit)
- [Sensors](https://github.com/vbodenstein/Chaotic-Pendulum-Encrytion#sensors)
- [Labjack Control and Code](https://github.com/vbodenstein/Chaotic-Pendulum-Encrytion/blob/main/README.md#labjack-and-code)
- [Control of Pendulum](https://github.com/vbodenstein/Chaotic-Pendulum-Encrytion/blob/main/README.md#control-of-pendulum)
    - [Motion](https://github.com/vbodenstein/Chaotic-Pendulum-Encrytion/blob/main/README.md#testing-and-changes)
    - [Testing](https://github.com/vbodenstein/Chaotic-Pendulum-Encrytion/blob/main/README.md#randomness)
    - [Randomness]
-[Encryption Method]
- [Results](https://github.com/vbodenstein/Chaotic-Pendulum-Encrytion/blob/main/README.md#results)
    - [Example 1](https://github.com/vbodenstein/Chaotic-Pendulum-Encrytion/blob/main/README.md#examples)
    - [Example 2]
    - [Example 3]
- [Conclusion](https://github.com/vbodenstein/Chaotic-Pendulum-Encrytion/blob/main/README.md#conclusion)



# Budget

| Part  | Quantity | Cost |
| ------------- | ------------- | ------------- |
| DC Gear Motor  | 3  | $44.97 |
| Aluminium Rods  | 6  | $23.805 |
| Flanged Ball Bearings  | 5  | $36.91 |
| Bolts  | 20  | $11.50 |
| Screws  | 25  | $11. |
| Hall Effect Sensors  | 20  | $8.04 |
| Neodymium Magnets  | 18  | $7.82 |
| H-Bridge  | 5  | $11.5 |
| Solenoids  | 3  | $29.97 |




# Circuits 
For the setup we used three circuits, one to run the motor, another for the op-amp, and a third to connect three to four the sensors. 

### Motor circuit 

Using a DRV8833 motor driver we connect a 12V, 100RPM DC motor, this is then connected to a standard DC power supply.

Circuit Diagram             |  Physical
:-------------------------:|:-------------------------:
<img width="974" alt="Screen Shot 2023-05-15 at 5 27 41 PM" src="https://github.com/vbodenstein/Chaotic-Pendulum-Encrytion/assets/133536500/761e181d-c835-4561-83f3-1964c36d5877">  |  <img width="380" alt="Screen Shot 2023-06-07 at 1 44 44 PM" src="https://github.com/vbodenstein/Chaotic-Pendulum-Encrytion/assets/133536500/dfcd8c5d-4844-43e7-b7f6-bded4390f2a8">




### Sensor Circuit

Circuit Diagram             |  Physical
:-------------------------:|:-------------------------:
![circuit](https://github.com/vbodenstein/Chaotic-Pendulum-Encrytion/assets/133536500/f747b40a-b0e2-493b-96f8-a94cdae36696)  |  <img width="408" alt="Screen Shot 2023-06-07 at 1 44 36 PM" src="https://github.com/vbodenstein/Chaotic-Pendulum-Encrytion/assets/133536500/2656bd21-4531-4f47-8fe4-42e9d1a0d6fb">



### Op-Amp Circuit

Linear Hall Effect Sensors are connect in a circuit with an op-amp


Circuit Diagram             |  Physical
:-------------------------:|:-------------------------:
!<img width="654" alt="Screen Shot 2023-06-07 at 1 05 00 PM" src="https://github.com/vbodenstein/Chaotic-Pendulum-Encrytion/assets/133536500/d66b2220-7c99-4e32-b2e1-29581b4d6da8">  |  !<img width="596" alt="Screen Shot 2023-06-07 at 1 41 58 PM" src="https://github.com/vbodenstein/Chaotic-Pendulum-Encrytion/assets/133536500/82695fac-90fd-4860-bd45-9a6716b4b97d">



## Sensors
Hall affect sensors detect the magnitude of a magnetic field using the Hall effect. We attach magents to the pendulum arms and as they swing past the sensors, we can pick up changes in voltage. The output from the sensor is called the Hall Voltage. 

:-------------------------:|:-------------------------:
<img width="934" alt="Screen Shot 2023-06-08 at 10 30 11 PM" src="https://github.com/vbodenstein/Chaotic-Pendulum-Encrytion/assets/133536500/eee6deb5-d757-47b1-ab5e-bad56ca11834"> | ![IMG_8422](https://github.com/vbodenstein/Chaotic-Pendulum-Encrytion/assets/133536500/9b7f8b0e-bdc5-4301-8646-e7768f052035)


# Control of Pendulum
We use a LabJack U3-HV and a DC Power Supply to control the motor and collect data. The process begins when a message is given to the program to be encrypted and initial conditions specified. Once the program is run, the pendulum begins oscillating until enough data is collected. 


### Motion

![Untitled design-7](https://github.com/vbodenstein/Chaotic-Pendulum-Encrytion/assets/133536500/7b1fa93a-b0d1-4735-992e-43c29964d53f)

We set up the pendulum on a 3D printed base. For the chaotic regimn, the ideal frequency is 3 Hz, this motion is shown above. The motor oscillates at 6 V, and 0.2 Amp.


![Untitled design-8](https://github.com/vbodenstein/Chaotic-Pendulum-Encrytion/assets/133536500/84e38877-7525-4d6a-bdcd-338ed04f42e3)


Here the pendulum is set to 2.5 Hz, 6 V, 0.2 A. The motion is periodic, as there is not enough energy supplied by the motor to cause divergence. To find these two regimns we tested the pendulum at various frequencies and voltages. These numbers are specific to the setup.



### Testing and Changes 

The raw hall affect data:

Full Running Time          |  5-10 sec                 | 5-10 sec
:-------------------------:|:-------------------------:|:-------------------------:
![RawData2](https://github.com/vbodenstein/Chaotic-Pendulum-Encrytion/assets/133536500/2e1e69ca-5e45-4119-9946-db18a0fd5c2b)  |  ![RawDataChaotic2](https://github.com/vbodenstein/Chaotic-Pendulum-Encrytion/assets/133536500/66dc4f40-acb3-436a-808e-b154a636f8e1) | ![RawDataOrder2](https://github.com/vbodenstein/Chaotic-Pendulum-Encrytion/assets/133536500/bdf087de-5636-48bd-90f2-11e6a4a23b45)

We plot the direct voltage picked up by the hall affect sensors. Here is another example of what the output may look like:


![RawDataChaotic3](https://github.com/vbodenstein/Chaotic-Pendulum-Encrytion/assets/133536500/c2c9c810-e2b3-4dd7-b9a6-92ff752de23f)


From here we filter the data to further understand where the chaotic motion is occuring and its magnitude. The low pass filter takes the large spikes out of the picture:

<img width="553" alt="Screen Shot 2023-06-07 at 2 07 03 PM" src="https://github.com/vbodenstein/Chaotic-Pendulum-Encrytion/assets/133536500/dc70b951-85e4-44c9-862b-23aa1bd468d4">


Using the low pass filter we get much clearer data which looks like this:


Full Running Time          |  5-10 sec                 | 5-10 sec
:-------------------------:|:-------------------------:|:-------------------------:
![Filtered4](https://github.com/vbodenstein/Chaotic-Pendulum-Encrytion/assets/133536500/0a899d9f-a1aa-4c3b-be39-dc0cdcc0a18d)  |  ![FIlteredChaotic4](https://github.com/vbodenstein/Chaotic-Pendulum-Encrytion/assets/133536500/cdaf73c0-fd90-49a1-ad2e-9450ac9ee285) | ![FilteredDataOrdered2](https://github.com/vbodenstein/Chaotic-Pendulum-Encrytion/assets/133536500/5f61d397-ff19-4b6f-ac74-e3154c0f709c)


We look for regions where the motion is not sinusoidal, maybe it is cubic or quadratic; generally the random motion causes discrepencies in the sine wave. 

The next step is to set a boundry, and let anything below the boundry be a one, and everything above the boundry be a zero. 


<img width="1364" alt="Screen Shot 2023-06-07 at 2 17 11 PM" src="https://github.com/vbodenstein/Chaotic-Pendulum-Encrytion/assets/133536500/d0e13027-eba7-442d-b29d-715b2a2b2c07">


From here we can finally extract data by comaring the distance between peaks in the chaotic vs sinusoidal motion producing a sequence of zeros and ones. In theory, the sine wave should give a repeating sequence of 1-0-1-0, or even a more complicated repeating pattern. The chaotic motion should produce a random sequence. 

Full Running Time          |  5-10 sec                 | 5-10 sec
:-------------------------:|:-------------------------:|:-------------------------:
![NormalizedData1](https://github.com/vbodenstein/Chaotic-Pendulum-Encrytion/assets/133536500/05481b93-5f7a-4c35-a2c6-95c38ee39646)  |  ![NormalChaotic4](https://github.com/vbodenstein/Chaotic-Pendulum-Encrytion/assets/133536500/6fd15be6-2708-4962-a3f4-433827fa685e) | ![NormalizedOrder3](https://github.com/vbodenstein/Chaotic-Pendulum-Encrytion/assets/133536500/32168acf-ef87-4a53-84ff-b57c9eeab0ad)



### Randomness 

There are a few places to look for randomness when looking at the data collected by the sensors. To test this we do a FFT. Here the choatic motion produces significantly more noise, as expected. 


<img width="517" alt="Screen Shot 2023-06-07 at 2 27 47 PM" src="https://github.com/vbodenstein/Chaotic-Pendulum-Encrytion/assets/133536500/bf199c52-9fe9-4736-a009-6ccd47869d75">



# Encryption Method

For this project, we use a stream cipher with an XOR operator between the plaintext and key. Particularly we used the One-Time Pad (OTP) encryption system. The XOR operator is defined as follows:

<img width="327" alt="Screen Shot 2023-06-08 at 6 55 03 PM" src="https://github.com/vbodenstein/Chaotic-Pendulum-Encrytion/assets/133536500/e414eacb-d78d-43c2-887c-4b7625e3085a">

To make the OTP secure, the key must be at least the length of the message, and each key must be unique. If the late is violated, then it is possible to crack the encryption. 
 
The OTP was used because, personally, I really like the idea that a One Time Pad is unbreakable. Even though in practice it is considered malleable, the encryption itself is perfect. A [University of Chicago lecture](https://www.google.com) shows a proof for the OTP's perfectly secure encryption, as well as other things. Note: many times rather than using a true OTP, random number generators, in essence, stretch out a sequence of random numbers to match the length of the message. This is however unsafe since these number generators are actually deterministic, at least to some extent. 


# Results


### Example One:

**Message we gave the system to encrypt:** Against stupidity the Gods themselves contend in vain.

**Binary Output:**

000101010110101010110101011010101110010101100111101010011101011011101010010000100110011101101000000001001110011001111100110001110101101010010101001001001001101001100110101010010110101010100100101001111111101010100010100010101010011100110010101001001010100110101010100110110001010110101010100111. . . . . 


**This is converted into a key:**

\x01V\xabV\xaeVz\x9dn\xa4&v\x80Ng\xccu\xa9RI\xa6j\x96\xaaJ\x7f\xaa(\xaas*J\x9a\xa9\xb1Z\xa9\xe5\xab\xaa\xb7\x96[\xb5\x98\xdav\xee\xa2\xb5G*\x1d\xca\xaa\xe5pBf\xe8\xd6c\x1b\x1e2+J\xb3\x00\x88\xa6UZW\xaa)H\x8a'


**The encrypted data is:** \x17\xcc7\xc78\t\xe9N\xd7R\x03\xf0'\x03\xa5\x01\xd0r=\xce\x0f\xb6\xed%\x1b\xd9\x08\xde\x1bO'\xe9\xcc\xdd,\xcc\x96\x8b\xc9\xd8\xf8/\xd0\xf6\xbeV\x87\xcc\x951Kt\xa4\x84

**The decrypted data is:**  Against stupidity the Gods themselves contend in vain.



### Second Run, Same Message:

**Output Binary:**
111000100110100010010010010100101000010010010010101010010010101101001010010011010010101000110010010010100001000000100011010001000000100011000000010101010101010010101010010001101011101010011101010000100110010100101100100100100001000011000011010001001101001010001100010000101000101000110000. . . .

**Key:** q4I)BIT\x95\xa5&\x95\x19%\x08\x11\xa2\x04`*\xaaU#]N\xa12\x96I\x08a\xa2iF!E\x18\x04\x8a\x86"\x12Q\xa2\x8e%ZE\x10\x92\xa5EUZ$\x86\xe4\x8ayQ\x85\x86\x82\xd2T\x88D\x96)F\x8c(\x84eSn\x88A\x95$\x9c\x91\xa2EUD\x18\x96


#### Encrypted Data:
Qu.H+''\xe1\x85U\xe1lUau\xcbpx19\n\xde=F}\txceV\xe5i|\t\xc7\x045D)na\xf9\xa6A}?\xd6\xebK>eyxfc\x85343J\xa8



### Example Two:

We can compare the normalizad data for the ordered motion vs. the chaotic motion. This run gave us the expected pattern for the ordered data, with a few areas of deviation.

#### Ordered:

0101010101010101010101010101010101010101010101010101010010101010101010001010101010101010101010111010100010101011010101010101010101010101010101010

#### Chaotic:

11000100001010101001010100000000011000101000101010101000001001100010010100100010001101000000110100000000001001000100100000001000100010100000001


#### Encryption with the chaotic:

#### The key:

b'b\x15J\x801ET\x13\x12\x91\x1a\x06\x80\x12$\x04E\x01' 

#### Encrypted Message: 

B}/\xec]*#3e\xfehj\xe4



### Example three (for data view Data.4):

#### Message to Encrypt:

Abracadabra

 
#### Chaotic:

110110010001000001001110101001001001001100001010010011100011000100100010100110101010010001001001010100101010110000101010101001000000010100


#### Key:

\x03dA:\x92L)8\xc4\x8aj\x91%J\xb0\xaa\x90\x14

#### The encrypted data is:

#%#H\xf3/H\\a5xe8\rd14x0





#### Ordered:
 
1101110010011100110111001100110011011100100110011000110111001100110011001100110011001100110011010000110010001100110111001100110011001100110011001100110011001


#### Key: 

\x1b\x93\x9b\x99\x9b\x931\xb9\x99\x99\x99\x99\xa1\x91\x9b\x99\x99\x99\x99\x99 

#### The encrypted data is: 

Z\xf1\xe9\xf8\xf8\xf2U\xd8\xfb\xeb\xf8



Notice: the repetition in the ordered sequence as apposed to the chaotic sequence for the encrypted data.

# Conclusion
![Untitled design-7](https://github.com/vbodenstein/Chaotic-Pendulum-Encrytion/assets/133536500/8ae67c65-96d8-4c53-b858-4c43000a5661)

In this project we successfully created a chaotic system and used it to encrypt and decrypt messages. The level of "randomness" in the keys generated depends greatly on the frequency of oscillation, as we saw by comparing 3.0 Hz and 2.5 Hz oscillations. The messages encrypted with the choatic regimn (3.0 Hz) show significantly less repitition than those encrypted with the 2.5 Hz when comparing the raw data, and the encrypted messages. 

While building this project, we found that the use of hall effect sensors is not recommended for such a set up, they break very easily and don't produce large enough deviations from the noise. Changing the way we detect the motion would increase the efficiency, and amount of time it takes to produce data. The next thing to focus on would be the rate at which we aquire random data. Currently, it takes approximately five mintues to encrypt a single sentence--say of this size. In practice, this is very slow, so increasing the number of sensors, and analyzing the data in a more effective way could produce much faster encryption. Another way to increase speed is by exploring more efficient cryptographic alternatives for example, public key encryption.

The great thing is that with the chatoic system, the key will obvioulsy not be guessed. Hypothetically if we use the sinusoidal wave for encryption we get a string of zeros and ones, which will encrypt the message without problems. Obviously this is not safe since it is very easy to deduce they key and is susceptible to hackers, so the more random the key, the better the encryption. 

Overall, we show that a double pendulum can be a successful random number generator for encryption. The symmetric stream cipher is only one method of using the collected data for encryption. Combined with an alternate cryptographic system and nicer sensors, a double pendulum could be a viable candidate for secure encryption. 
