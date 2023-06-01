# Chaotic-Pendulum-Encrytion
This is the project page for our Chatoic Pendulum Encrytion system. A driven double pendulum is by nature a chaotic system, meaning it is highly dependent on, and sensitive, to initial conditions. Utilizing this fact, we can extract sequences of numbers producing a randomized key. Each time the pendulum starts, it’s path will be different unless the starting conditions are exactly identical. In a physical system however, this is nearly impossible, making it an interesting case for encryption. Using hall affect sensors we detect when the pendulum passes certain positions and use this to encode a cipher.

<img width="464" alt="Screen Shot 2023-05-31 at 3 39 20 PM" src="https://github.com/vbodenstein/Chaotic-Pendulum-Encrytion/assets/133536500/2b350b04-814d-4dde-95a9-716105cc330e">


## Table of contents
- [Budget](https://github.com/vbodenstein/Chaotic-Pendulum-Encrytion/blob/main/README.md#budget)
- [Circuits](https://github.com/vbodenstein/Chaotic-Pendulum-Encrytion/blob/main/README.md#circuits)
    - [Motor](https://github.com/vbodenstein/Chaotic-Pendulum-Encrytion/blob/main/README.md#motor-circuit)
    - [Sensor](https://github.com/vbodenstein/Chaotic-Pendulum-Encrytion/blob/main/README.md#sensor-circuit)
    - [Op-amp](https://github.com/vbodenstein/Chaotic-Pendulum-Encrytion/blob/main/README.md#op-amp-circuit)
- [Labjack Control and Code](https://github.com/vbodenstein/Chaotic-Pendulum-Encrytion/blob/main/README.md#labjack-and-code)
- [Pendulum Control](https://github.com/vbodenstein/Chaotic-Pendulum-Encrytion/blob/main/README.md#control-of-pendulum)
    - [Tests](https://github.com/vbodenstein/Chaotic-Pendulum-Encrytion/blob/main/README.md#testing-and-changes)
    - [Randomness](https://github.com/vbodenstein/Chaotic-Pendulum-Encrytion/blob/main/README.md#randomness)
- [Sensor Data](https://github.com/vbodenstein/Chaotic-Pendulum-Encrytion/blob/main/README.md#sensor-data)
- [Results](https://github.com/vbodenstein/Chaotic-Pendulum-Encrytion/blob/main/README.md#results)
    - [Examples](https://github.com/vbodenstein/Chaotic-Pendulum-Encrytion/blob/main/README.md#examples)
- [Conclusion](https://github.com/vbodenstein/Chaotic-Pendulum-Encrytion/blob/main/README.md#conclusion)


## Budget

| Part  | Quantity | Cost |
| ------------- | ------------- | ------------- |
| DC Gear Motor  | 3  | $44.97 |
| Aluminium Rods  | 6  | Third Header |
| Flanged Ball Bearings  | 5  | $36.91 |
| Bolts  | 20  | $11.50 |
| Screws  | 25  | $11. |
| Hall Effect Sensors  | 20  | $8.04 |
| Neodymium Magnets  | 18  | $7.82 |
| H-Bridge  | 5  | $11.5 |
| Solenoids  | 3  | $29.97 |




## Circuits 

### Motor circuit 
Using a DRV8833 motor driver we connect a 12V, 100RPM DC motor

<img width="974" alt="Screen Shot 2023-05-15 at 5 27 41 PM" src="https://github.com/vbodenstein/Chaotic-Pendulum-Encrytion/assets/133536500/761e181d-c835-4561-83f3-1964c36d5877">



### Sensor Circuit

![circuit](https://github.com/vbodenstein/Chaotic-Pendulum-Encrytion/assets/133536500/f747b40a-b0e2-493b-96f8-a94cdae36696)


### Op-Amp Circuit

<img width="980" alt="Screen Shot 2023-05-30 at 11 40 56 AM" src="https://github.com/vbodenstein/Chaotic-Pendulum-Encrytion/assets/133536500/95555882-8c0f-4dd4-89f7-c37b6799e240">



# LabJack and Code
We use a LabJack U3-HV to control the motor and collect data. 



The process begins when a message is given to the program to be encrypted and initial conditions specified
(though, in reality, the latter in unnecessary because each time they will be inherently different anyways). Once
the device is triggered, the fixed positions of the arms are released and the motor begins oscillating. The hall affect
sensors on the surface walls will collected data by running a stream where each time the magnets on the pendulum
pass near the sensor the stream output will read one where otherwise it will read zero (the sensors will likely begin
collecting data after a brief period of time so that the system will already have diverged for non-identical initial
conditions. This allows for more variability in the first portion of the key).


### Control of Pendulum

### Testing and Changes 

Plot for cuttoff voltage value:


<img width="369" alt="Screen Shot 2023-05-24 at 11 16 13 AM" src="https://github.com/vbodenstein/Chaotic-Pendulum-Encrytion/assets/133536500/8978d65a-e768-4b37-9f1a-3c9e2ca1ad8a">



### Randomness



# Sensor Data




# Encryption Results


### Examples

(CHANGE)
In this variation, we will use the known XOR operator used in stream ciphers. It goes as follows.

Text: Hello World:
0100100001100101011011000110110001101111001000000101011101101111011100100110110001100100

Key Generated by our chaotic device:
0011001000110100001101100011000000110000001110010011010000110100001100000011100000111000

Ciphertext:
0111101001010001010110100101110001011111000110010110001101011011010000100101010001011100

Translates:
zQZ c[BT

In this example the text is short so the chaotic system wouldn’t need to run for very long, the whole process
would be done quite fast.






# Conclusion
