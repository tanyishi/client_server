from flask import Flask, request, render_template
info=36.1
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('test.html',temper=info)


if __name__ == '__main__':
    app.run(port=5002, debug=True, host='0.0.0.0') 



