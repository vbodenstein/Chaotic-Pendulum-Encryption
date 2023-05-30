import random
import matplotlib.pyplot as plt
import numpy as np
import u3
import time


d = u3.U3()
def setFIO(speed1, speed2):
    d.getFeedback(u3.Timer0Config(TimerMode = 0, Value = int((1-speed1)*65535)))
    d.getFeedback(u3.Timer1Config(TimerMode = 0, Value = int((1-speed2)*65535)))
