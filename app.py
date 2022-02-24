from flask import Flask

app = Flask(__name__)

#welcome page
@app.route('/')
def welcome():
    return 'Welcome to YouVlog!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
