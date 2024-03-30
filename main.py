import serial
from vpython import *  # Assuming you are using Visual Python for visualization
import time
import numpy as np

# Establish serial connection with Arduino
arduinoData = serial.Serial('/dev/cu.usbmodem12401', 115200)
time.sleep(1)  # Allowing time for the connection to stabilize

# Setting up the scene
scene.range = 5
scene.forward = vector(-1, -1, -1)
scene.width = 600
scene.height = 600

# Creating arrows for visualization
xArrow = arrow(axis=vector(1, 0, 0), length=2, shaftwidth=.1, color=color.red)
yArrow = arrow(axis=vector(0, 1, 0), length=2, shaftwidth=.1, color=color.green)
zArrow = arrow(axis=vector(0, 0, 1), length=2, shaftwidth=.1, color=color.blue)

frontArrow = arrow(axis=vector(1, 0, 0), length=4, shaftwidth=.1, color=color.purple)
upArrow = arrow(axis=vector(0, 1, 0), length=1, shaftwidth=.1, color=color.magenta)
sideArrow = arrow(axis=vector(0, 0, 1), length=2, shaftwidth=.1, color=color.orange)

# Creating objects for visualization
bBoard = box(length=6, width=2, height=.2, opacity=.8, pos=vector(0, 0, 0))
arduinoBox = box(length=1.75, width=.6, height=.1, pos=vector(-2, .1 + .05, 0), color=color.green)
bnoBox = box(length=1, width=.75, height=.1, pos=vector(-.5, .1 + .05, 0), color=color.blue)
myObj = compound([bBoard, arduinoBox, bnoBox])

while True:
    try:
        # Wait for data from Arduino
        while arduinoData.inWaiting() == 0:
            pass

        # Read data from Arduino
        dataPacket = arduinoData.readline().decode('utf-8').strip()
        splitPacket = dataPacket.split(',')

        # Extract quaternion data from the packet
        q0, q1, q2, q3 = map(float, splitPacket)

        # Convert quaternion to Euler angles
        roll = -atan2(2 * (q0 * q1 + q2 * q3), 1 - 2 * (q1 * q1 + q2 * q2))
        pitch = asin(2 * (q0 * q2 - q3 * q1))
        yaw = -atan2(2 * (q0 * q3 + q1 * q2), 1 - 2 * (q2 * q2 + q3 * q3)) - np.pi / 2

        # Update visualization
        rate(50)  # Limiting the visualization update rate
        k = vector(cos(yaw) * cos(pitch), sin(pitch), sin(yaw) * cos(pitch))
        y = vector(0, 1, 0)
        s = cross(k, y)
        v = cross(s, k)
        vRot = v * cos(roll) + cross(k, v) * sin(roll)

        frontArrow.axis = k
        sideArrow.axis = cross(k, vRot)
        upArrow.axis = vRot
        myObj.axis = k
        myObj.up = vRot
        frontArrow.length = 4
        sideArrow.length = 2
        upArrow.length = 1

    except Exception as e:
        print("An error occurred:", e)
        # Add proper error handling here if needed
