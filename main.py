from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Web App with Python Flask!\n'

if __name__ == '__main__':
    print('wow, nechego sebe vot eto da')
    
