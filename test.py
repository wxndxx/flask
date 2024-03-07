from flask import Flask
import sys
import time

app = Flask(__name__)

@app.route('/')
def index():
    for i in range(10):
        print('Error message', file=sys.stderr)
    return 'wow, nechego sebe vot eto da\n'

if __name__ == '__main__':
    print('wow, nechego sebe vot eto da')
