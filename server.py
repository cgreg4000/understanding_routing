from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<string:name>')
def say(name):
    return f"Hi {name.capitalize()}!"


@app.route('/repeat/<int:times>/<string:text>')
def repeat(times, text):
    return f"{text * times}"

@app.route('/<path:path>')
def no_page(path):
    return f"Sorry! No response. Try again."

if __name__ == "__main__":
    app.run(debug = True)