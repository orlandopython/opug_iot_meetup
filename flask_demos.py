from nest_demos import *
from milight_demos import *
from flask import Flask, abort

app = Flask(__name__)
lamp = init_lights()
napi = init_nest()


@app.route("/")
def hello():
    return "Hello OPUG"


@app.route("/lightsoff")
def route_lightsoff():
    lights_off(lamp)
    return "Lights Off"


@app.route("/lights")
def route_light():
    lights_on(lamp)
    return "Lights On"

@app.route("/lights/<state>")
def route_light_switch(state):
    if state == "on":
        return route_light()
    elif state == "off":
        return route_lightsoff()
    else:
        abort(404)

@app.route("/home")
def route_nest_home():
    nest_set_away(napi, False)
    return "WELCOME HOME"

@app.route("/nest/<int:temp>")
def route_nest_temp(temp):
    set_nest_temp(napi, temp)
    return "DONE"

@app.route("/nest")
def route_nest_get_temp():
    return "Current temp %d" % get_nest_temp(napi)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=1)

