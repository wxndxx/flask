from flask import Flask
import sys
import time

app = Flask(__name__)

@app.route('/')
def index():
    while True:
        time.sleep(1)
        print('Error message', file=sys.stderr)
    return 'wow, nechego sebe vot eto da\n'

if __name__ == '__main__':
    print('wow, nechego sebe vot eto da')
