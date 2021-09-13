## About
In this project my primary goal is to create a IoT environment to keep track of room temperature and humidity. While trying to do so, I have also maximized the number of parts used.

I shall now describe the usage of each individual parts that I have employed in the project.

1. DHT sensor: To measure temperature and humidity
2. LEDs: To indicate changes in temperature (bright red to indicate extremities)
3. Buzzer: To alarm residents whenever humidity gets too high or too low
4. ESP32: To record the data, interact with sensors and upload the records to a cloud storage

## Functionality
We use `micropython` to code for the project. It can be found in the `./main.py` file present in the folder.

**Instructions to run the code**:

- `sudo pip install esptool` to install esptool
- `esptool.py --port /dev/ttyUSB0 erase_flash`
- `esptool.py --chip esp32 --port /dev/ttyUSB0 write_flash -z 0x1000 esp32-20210912-unstable-v1.17-20-g0a5107372.bin` the binary file mentioned here is required to be downloaded and wrt this project can be found in the `./bin/` folder.
- `pip install adafruit-ampy`
- `sudo chmod 777 /dev/ttyUSB0`
- To finally run the program use `ampy --port /dev/ttyUSB0 --baud 115200 run main.py`

The ESP32 takes in data from the DHT sensor (temp, humidity) and then activates the LEDs and Buzzer based on the measured data. This data is also further reported to the thinkspeak channel via an api call.
