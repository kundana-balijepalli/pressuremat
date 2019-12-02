import serial
import numpy as np
import select, sys, time
import matplotlib.pyplot as plt
import matplotlib.animation as am
from scipy import signal
import numpy as np

#configuring serial port
arduinoData = serial.Serial('COM6', baudrate = 500000)


#initializing a matrix
w, h = 23,22
matrix = np.zeros(shape = (w,h))


#notch filter
fs = 200 #sample freq
f0 = 60 #power line interference
Q = 30 #quality factor


b,a = signal.irrnotch(f0,Q,fs)

def generate_data():
    while(arduinoData.inWaiting() == 0):
        pass
    try:
        for j in range(w):
            arduinoString = arduinoData.readline().decode('ascii')
            dataArray = arduinoString.split()
            Array = [int(k) for k in dataArray]
            for i in range(h):
                matrix[j][i] = Array[i]
        print(matrix)
        print("")
        return(matrix)
    except:
        print('Keyboard interrupt')
    
def update(data):
    mat.set_data(data)
    return mat

def data_gen():
    while True:
        yield generate_data()


fig, ax = plt.subplots() #create a figure and set a subplot
mat = ax.matshow(generate_data(),vmin = 0, vmax = 1200) 
ax.autoscale(False)
plt.colorbar(mat)
ani = am.FuncAnimation(fig,update,data_gen)
plt.show()
            
