from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'wow, nechego sebe vot eto da\n'

if __name__ == '__main__':
    print('wow, nechego sebe vot eto da')
