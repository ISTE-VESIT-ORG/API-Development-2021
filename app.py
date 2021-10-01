from flask import Flask

# * Flask constructor takes the name of current module (__name__) as argument.
app = Flask(__name__)

# ? *** Base route ***
# * The route() function of the Flask class is a decorator 
# * it tells the application which URL should call the associated function.
@app.route('/')
def home():
    return "Hello there!"

# ? *** Driver function ***
if __name__ == "__main__":
    app.run(debug=True)
