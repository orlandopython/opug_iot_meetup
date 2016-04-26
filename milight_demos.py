from limitlessled.bridge import Bridge
from limitlessled.group.white import WHITE
import time

def init_lights(): 
    bridge = Bridge('192.168.12.247') 
    bridge.incr_active()
    return bridge.add_group(1, 'demo', WHITE)

def lights_off(light):
    light.on = False;

def lights_on(light):
    light.on = True;


def light_brightness(light, level):
    light.brightness = level 

def light_temperature(light, color):
    light.temperature = color


if __name__ == '__main__':
    demo = init_lights()
    lights_on(demo)
    light_temperature(demo, 0)
    light_brightness(demo, 0)
    #demo.transition(5, brightness=1)
    time.sleep(2)
    light_brightness(demo, 0.5)
    light_temperature(demo, 1)

    time.sleep(2)
    light_brightness(demo, 1)
    lights_off(demo)
