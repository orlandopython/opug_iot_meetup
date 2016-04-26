
# Nest 

Nest Home Simulator Chrome Extension

If you don't have a Nest, but still want to try stuff out, Nest provides a cool chrome extension to make "fake" Nest devices under a developer account. 

 * [https://developers.nest.com/documentation/cloud/home-simulator/](https://developers.nest.com/documentation/cloud/home-simulator/) 
 * Must have developer account. 
 * Can create all the fake devices you want.
 * Can see status on https://home.nest.com like a normal Nest.

## python-nest library

[https://github.com/jkoelker/python-nest/](https://github.com/jkoelker/python-nest/)

Great library with solid API coverage for thermostats, but currently missing Camera support.
    * `pip install python-nest`
    * Can control all devices on your account.
    * There may be a better library out there, but I haven't found it yet.
    
```python
import nest

username = 'joe@user.com'
password = 'swordfish'

napi = nest.Nest(username, password)

for structure in napi.structures:
    print 'Structure %s' % structure.name
    print '    Away: %s' % structure.away
    print '    Devices:'

    for device in structure.devices:
        print '        Device: %s' % device.name
        print '            Temp: %0.1f' % device.temperature
```


# Milight / LimitlessLED

LimitlessLED makes really great and cheap remote control LED light bulbs. Much cheaper than Hue. Pretty widely available now and include a [developer portal on their website](http://www.limitlessled.com/dev).

 * [http://www.limitlessled.com/](http://www.limitlessled.com/)
 * Quite a few libraries out there to use them.
 * Repackaged under a few different names such as LimitlessLed, Milight, Easybulb, applight, dekolight and iLight.
 * Restore previous state on power up! (In your face Hue)
 * Requires bridge product to use over internet or on local network.

## python-limitlessled library

[https://github.com/happyleavesaoc/python-limitlessled](https://github.com/happyleavesaoc/python-limitlessled)
This is probably the best library I've used for these bulbs that has both Python 2 & 3 support.

 
 * `pip install limitlessled`
 * Supports white, and RGBW bulbs.
 * Up to 4 white zones per bridge AND 4 color zones per bridge.
 
```python
from limitlessled.bridge import Bridge
from limitlessled.group.rgbw import RGBW

bridge = Bridge('<your bridge ip address>')
bedroom = bridge.add_group(1, 'bedroom', RGBW)
bedroom.on = True
bedroom.brightness = 0.5 # 0.0 through 1.0
bedroom.temperature = 0.6 # 0.0 through 1.0
```


 

# Flask

Python webserver microframework. [http://flask.pocoo.org/](http://flask.pocoo.org/)

 * Built in development server 
 * Jinja template engine
 * Tons of addons
 * `pip install Flask`

Super simple, super minimal.

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
```

To add routes, just add another route function and the `@app.route(...)` decorator before `app.run()`.

```python
@app.route("/meetup")
def meetup():
    return "Orlando Python User Group is the best!"
```


## WeMo

Ouimeaux library has a lot of functionality to it.

[http://ouimeaux.readthedocs.org/en/latest/](http://ouimeaux.readthedocs.org/en/latest/
)

 * Comes with webserver and web app to connect and run WeMo's and python API
 * `pip install ouimeaux`

