# Setup

    sudo create_ap wlp0s20u2 wlp4s0 PythonThings orlandopython
    create_ap --list-running
    create_ap --list-clients <id>


# Nest 

Nest Home Simulator Chrome Extension

 * Must have developer account. 
 * Can create all the fake devices you want.
 * Can see status on https://home.nest.com

## python-nest library on pypi
    pip install python-nest
    python
    import nest


## Flask

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

