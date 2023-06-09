#Creating the chatoic data set --with a delay condition
numsOrdered = getData(0.25,200)
time.sleep(5)
numsChaotic = getData(0.20,200) 

#plotting the raw data
fig, axs = plt.subplots(2,1, sharex=True, sharey=True)
fig.supxlabel('Time [sec]')
fig.supylabel('Measured Voltage (V)')
axs[0].plot(np.arange(1,len(numsOrdered)+1)[10:]/100,numsOrdered[10:], label = 'Sinusoidal Behavior')
axs[1].plot(np.arange(1,len(numsChaotic)+1)[10:]/100,numsChaotic[10:], color = 'red', label = 'Chaotic Behavior')
fig.legend(loc=1)
fig.tight_layout(rect=[0, 0, 1, 0.9])
plt.show()

plt.plot(np.arange(1,len(numsChaotic)+1)[10:]/100,numsChaotic[10:], color = 'red')
plt.xlim(5,10)
plt.ylim(0.45, 0.6)
plt.xlabel('Time [sec]')
plt.ylabel('Voltage [V]')
plt.title('Raw Data Chatoic')
plt.show()

plt.plot(np.arange(1,len(numsChaotic)+1)[10:]/100,numsChaotic[10:], color = 'red')
plt.xlim(10,15)
plt.xlabel('Time [sec]')
plt.ylabel('Voltage [V]')
plt.title('Raw Data Chatoic')
plt.show()

plt.plot(np.arange(1,len(numsOrdered)+1)[10:]/100,numsOrdered[10:], color = 'blue')
plt.xlim(5,10)
plt.xlabel('Time [sec]')
plt.ylabel('Voltage [V]')
plt.title('Raw Data Sinusoidal')
plt.show()

plt.plot(np.arange(1,len(numsOrdered)+1)[10:]/100,numsOrdered[10:], color = 'blue')
plt.xlim(10,15)
plt.xlabel('Time [sec]')
plt.ylabel('Voltage [V]')
plt.title('Raw Data Sinusoidal')
plt.show()




#filtering the data with a low pass and ploting the filtered data
filts1, diffs1 = filterData(5, numsOrdered)
filts2, diffs2 = filterData(5, numsChaotic)

fig, axs = plt.subplots(2,1, sharex=True, sharey=True)
fig.supxlabel('Time [sec]')
fig.supylabel('Effective Magnitude')
axs[0].plot(np.arange(1,len(filts1)+1)/100,1000*filts1, label = 'Sinusoidal Behavior')
axs[1].plot(np.arange(1,len(filts2)+1)/100,1000*filts2, color = 'red', label = 'Chaotic Behavior')
fig.legend(loc=1)
fig.tight_layout(rect=[0, 0, 1, 0.9])
plt.show()

plt.plot(np.arange(1,len(filts2)+1)/100,1000*filts2, color = 'red')
plt.xlim(5,10)
plt.xlabel('Time [sec]')
plt.ylabel('Threshold')
plt.title('Filtered Data Chaotic')
plt.show()

plt.plot(np.arange(1,len(filts2)+1)/100,1000*filts2, color = 'red')
plt.xlim(10,15)
plt.xlabel('Time [sec]')
plt.ylabel('Threshold')
plt.title('Filtered Data Chaotic')
plt.show()


plt.plot(np.arange(1,len(filts1)+1)/100,1000*filts1, color = 'blue')
plt.xlim(5,10)
plt.xlabel('Time [sec]')
plt.ylabel('Threshold')
plt.title('Filtered Data Sinusoidal')
plt.show()

plt.plot(np.arange(1,len(filts1)+1)/100,1000*filts1, color = 'blue')
plt.xlim(10,15)
plt.xlabel('Time [sec]')
plt.ylabel('Threshold')
plt.title('Filtered Data Sinusoidal')
plt.show()



#generating the random set of data with from the filter and plotting the normalized data
peaks1, bits1, data1 = genRand(filts1)
peaks2, bits2, data2 = genRand(filts2)

fig, axs = plt.subplots(2,1, sharex=True, sharey=True)
fig.supxlabel('Time [sec]')
fig.supylabel('Threshold')
axs[0].plot(np.arange(1,len(peaks1)+1)/100,peaks1, label = 'Ordered Behavior')
axs[1].plot(np.arange(1,len(peaks2)+1)/100,peaks2, color = 'red', label = 'Chaotic Behavior')
fig.legend(loc=1)
fig.tight_layout(rect=[0, 0, 1, 0.9])
plt.show()


plt.plot(np.arange(1,len(peaks2)+1)/100, peaks2, color = 'red')
plt.xlim(5,10)
plt.xlabel('Time [sec]')
plt.ylabel('Threshold')
plt.title('Normalized Data Chaotic')
plt.show()

plt.plot(np.arange(1,len(peaks2)+1)/100, peaks2, color = 'red')
plt.xlim(10,15)
plt.xlabel('Time [sec]')
plt.ylabel('Threshold')
plt.title('Normalized Data Chaotic')
plt.show()

plt.plot(np.arange(1,len(peaks1)+1)/100,peaks1, color = 'blue')
plt.xlim(5,10)
plt.xlabel('Time [sec]')
plt.ylabel('Threshold')
plt.title('Normalized Data Sinusoidal')
plt.show()

plt.plot(np.arange(1,len(peaks1)+1)/100,peaks1, peaks2, color = 'blue')
plt.xlim(10,15)
plt.xlabel('Time [sec]')
plt.ylabel('Threshold')
plt.title('Normalized Data Chaotic')
plt.show()
