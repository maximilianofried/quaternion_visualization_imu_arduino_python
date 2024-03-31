# Real Time Quaternion Visualization with Arduino, IMU sensor and Python

## Overview

This project demonstrates how to visualize quaternion data from a 9-axis Inertial Measurement Unit (IMU) sensor connected to an Arduino using Python with Visual Python (VPython).

<div align="center">
   <img src="https://github.com/maximilianofried/quaternion-visualization-imu-arduino-python/assets/51124912/fcc3e1b0-813b-44c1-9d23-e7c1ad4f279e" alt="animated" />
</div>

## Table of Contents

- [Overview](#overview)
- [Setup](#setup)
- [Usage](#usage)
- [Dependencies](#dependencies)

## Setup

1. Connect the 9-axis IMU sensor to your Arduino.
2. Upload the provided `sketch.ino` to the Arduino.
3. Connect the Arduino to the appropriate serial port.
4. Install the required Python libraries using `pip install -r requirements.txt`.
5. Modify the Python script `main.py` to specify the correct serial port for your Arduino.

## Usage

1. Run the Python script `main.py`.
2. The script will establish a serial connection with the Arduino and initialize the visualization scene.
3. Quaternion data from the Arduino will be converted to Euler angles and used to update the visualization in real-time.

## Dependencies

- Python 3.x
- Visual Python (VPython)
- PySerial
