from machine import Pin, PWM
import dht, time, network, urequests

# Declaring constants
WIFI_NAME = "Papu"
WIFI_PASS = "Papiya@342"
SUBMIT_URI = "https://api.thingspeak.com/update?api_key=JLW0M9OJRRUT2IS3&"
sta_if = network.WLAN(network.STA_IF)
led = [Pin(4, Pin.OUT), Pin(18, Pin.OUT), Pin(21, Pin.OUT)]
buzzer = Pin(23, Pin.OUT)
dhtpin = Pin(2)

# Blinking LED
def blink(case):
    led[case].value(1)
    time.sleep(0.5)
    led[case].value(0)

# Ringing buzzer
def buzz():
    buzzer.value(1)
    time.sleep(0.5)
    buzzer.value(0)

# Dealing with sensor data
def activity(temp, humidity):
    # Make LED blink corresponding to temperature value
    if temp <= 15:
        blink(2)
    elif temp <= 30:
        blink(0)
    elif temp <= 35:
        blink(1)
    else:
        blink(2)
    # Ring the buzzer when humidity goes beyond threshold
    if humidity <= 10:
        buzz()
    elif humidity >= 80:
        buzz()

def report(temp, humidity):
    r = urequests.get(
        SUBMIT_URI
        + "field1="
        + str(temp)
        + "&field2="
        + str(humidity)
    )
    r.close()

# Get Measurement
def measurement(sen):
    sen.measure()
    return sen.temperature(), sen.humidity()

# Main Control Program
if __name__ == "__main__":
    print("WELCOME")
    print("--------")
    # Ensure ESP32 is connected to WiFi
    if not sta_if.isconnected():
        print("connecting to network...")
        sta_if.active(True)
        sta_if.connect(WIFI_NAME, WIFI_PASS)
        while not sta_if.isconnected():
            pass
    # Connection is succesfull
    print("Connected Successfully!")
    print("Network configuration:", sta_if.ifconfig())
    # Send sensor data
    sen = dht.DHT22(dhtpin)
    while True:
        temp, humidity = measurement(sen)
        activity(temp, humidity)
        report(temp, humidity)
        time.sleep(0.3)