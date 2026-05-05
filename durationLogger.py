import serial
import os
from datetime import datetime

ser = serial.Serial('COM3', 9600, timeout=1)

base_folder = "ToolDurationLogs"
os.makedirs(base_folder, exist_ok=True)

current_date = None
file = None

tool_on_time = None

def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

def get_filename():
    return datetime.now().strftime("log_%Y-%m-%d.csv")

def open_daily_file():
    global file, current_date

    new_date = datetime.now().strftime("%Y-%m-%d")

    if new_date != current_date:
        if file:
            file.close()

        current_date = new_date
        filepath = os.path.join(base_folder, get_filename())

        file_exists = os.path.isfile(filepath)
        file = open(filepath, "a")

        if not file_exists:
            file.write("OnTime,OffTime\n")

        print("Logging to:", filepath)

open_daily_file()

while True:
    try:
        open_daily_file()

        line = ser.readline().decode().strip()

        if not line:
            continue

        if line == "ON":
            tool_on_time = get_timestamp()
            print("ON :", tool_on_time)

        elif line == "OFF":
            off_time = get_timestamp()

            if tool_on_time:
                file.write(f"{tool_on_time},{off_time}\n")
                file.flush()
                print("OFF:", off_time)

            tool_on_time = None

    except KeyboardInterrupt:
        print("\nStopping logger...")
        if file:
            file.close()
        ser.close()
        break