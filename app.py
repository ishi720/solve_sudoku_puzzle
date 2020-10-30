from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    message = "Hello World"
    return render_template('index.html', title='test', message=message)

if __name__ == "__main__":
    app.run(debug=True)