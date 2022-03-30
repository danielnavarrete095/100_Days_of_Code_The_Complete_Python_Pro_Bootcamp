from flask import Flask
app = Flask(__name__)

def make_bold(function):
    def inner():
        return f'<b>{function()}</b>'
    return inner
def make_emphasis(function):
    def inner():
        return f'<em>{function()}</em>'
    return inner
def make_underlined(function):
    def inner():
        return f'<u>{function()}</u>'
    return inner

@app.route('/hello')
def hello_world():
    return "<h1>Hello World!</h1>"

@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def bye_world():
    return "<h1>Bye World!</h1>"

@app.route('/username/<name>')
def greet(name):
    return f"<h1>Hello {name+1}!</h1>"

if __name__ == '__main__':
    app.run(debug=True)