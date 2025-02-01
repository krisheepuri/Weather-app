from flask import Flask, render_template, request

app = Flask(__name__)  # Create an app

@app.route('/')
def home():
    return "Welcome to my website!"

if __name__ == '__main__':
    app.run(debug=True, port=8080)  # Start the server