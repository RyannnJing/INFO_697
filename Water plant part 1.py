'''
Introduction
Final project: test the plant environment and water the plant when it's dry.
The water level in a tank will be tested
Users will be noticed to add water to tank with the buzzer during day time.
Since it's not easy to get a water pump, I used the Red LED to mimic it.
For this part, I will do a pilot test of the sensors.
'''

import music
from microbit import *

# Set pins for sensors
water_sensor = pin0
ambient_light_sensor = pin1
soil_humidity_sensor = pin2
buzzer = pin12
# Red LED Module was used to mimic the water pump
relay = pin13

# Mian loop
def main():
    while True:
        display.clear()
        # Module output
        debug_output_module()
        # Get values from sensors
        w_level = get_sensor_analog(water_sensor, 'W')
        l_level = get_sensor_analog(ambient_light_sensor, 'L')
        h_level = get_sensor_analog(soil_humidity_sensor, 'H')
        msg = w_level + ',' + l_level + ',' + h_level
        display.scroll(msg)


# Module output
def debug_output_module():
    # Mimic the water pump
    relay.write_digital(True)
    sleep(1000*5)
    relay.write_digital(False)
    # Buzzer on
    music.play('f4:2', pin=buzzer, wait=True, loop=False)


# Get values from sensors
def get_sensor_analog(sensor, title):
    value = sensor.read_analog()
    content = title + ':' + str(value)
    return content

# Call the main function.
main()
