from flask import Flask

app = Flask(__name__)

# ? *** Base route ***
@app.route('/')
def home():
    return "Hello there!"

# ? *** Driver function ***
if __name__ == "__main__":
    app.run(debug=True)
