import serial
import os
from datetime import datetime

ser = serial.Serial('COM3', 9600)

base_folder = "ToolDurationLogs"
os.makedirs(base_folder, exist_ok=True)

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"session_{timestamp}.csv"
filepath = os.path.join(base_folder, filename)

file = open(filepath, "w")
file.write("Duration(s)\n")

print("Logging to:", filename)

while True:
    line = ser.readline().decode().strip()

    if not line or "Duration" in line:
        continue

    try:
        value = float(line)
        file.write(f"{value}\n")
        file.flush()
        print(value)
    except:
        pass