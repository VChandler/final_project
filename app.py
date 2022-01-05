from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def echo():
    return render_template('index.html', text="Final Project")

if __name__ == "__main__":
    app.run(debug=True)