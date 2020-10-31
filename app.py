from flask import Flask, render_template, jsonify
app = Flask(__name__)

@app.route('/')
def hello():
    message = "Hello World"
    return render_template('index.html', title='test', message=message)

@app.route('/api/')
def index():
    pazzle = [
        [0,5,9,0,3,0,7,2,0],
        [1,0,7,0,4,0,3,0,8],
        [0,6,0,2,0,5,0,4,0],
        [3,0,2,1,0,8,5,0,7],
        [0,1,0,7,0,6,0,3,0],
        [5,0,0,0,0,0,0,0,9],
        [0,0,4,0,0,0,6,0,0],
        [0,3,0,0,1,0,0,7,0],
        [7,0,1,5,6,4,2,0,3]
    ]

    return jsonify(pazzle)

if __name__ == "__main__":
    app.run(debug=True)