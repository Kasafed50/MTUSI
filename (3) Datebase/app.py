from flask import Flask, render_template

app = Flask(__name__)


@app.route('/login/', methods=['GET'])
def index():
    return render_template('login.html')


print('http://localhost:5000/login/')

if __name__ == '__main__':
    app.run()
