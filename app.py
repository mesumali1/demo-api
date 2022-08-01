from flask import Flask, request
app = Flask(__name__)

@app.route('/<name>')
def hello_name(name):
    return 'Hello ' + name + '!'

# @app.route('/mesum')
# def hello_mesum():
#     return 'Hello Mesum'


# @app.route('/shah')
# def hello_shah():
#     return 'Hello Shah'

if __name__ == '__main__':
 app.run()