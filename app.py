from flask import *
import random

app = Flask(__name__)

nameList = []
lordOfTheList = []

# ? *** Home ***
@app.route('/')
def home():
    return render_template("home.html")

# ? *** GET request ***
@app.route('/getName/<name>', methods=['GET'])
def getName(name):
    if request.method == 'GET':
        if name in nameList:
            return name
        return jsonify(lordOfTheList)
        # return jsonify({5: "Get request called"})

# ? *** Receive post request and store in array ***
@app.route('/insertName/<someString>', methods=['POST'])
def insertName(someString):
    if request.method == 'POST':
        nameList.insert(0, someString)

        # Append funny titles
        funnyTitles = ["Great", "Conquerer", "Magician", "Evolver","Depressed","Racist","Connoisseur"]
        title = funnyTitles[random.randint(0, len(funnyTitles)-1)]
        someString += " The "+title

        # Insert the new item in list
        lordOfTheList.insert(0, someString)
        
        return redirect(url_for("showRequests"))

        # ! alternative
        # return render_template("showRequest.html", lordOfTheList=lordOfTheList)

# ? *** Display contents from array ***
@app.route('/showRequests', methods=['GET'])
def showRequests():
    if request.method == 'GET':
        return render_template("showRequest.html", lordOfTheList=lordOfTheList)

# ? *** Backgroung processes ***
@app.route('/background_process', methods=['GET'])
def background_process():
    if request.method == 'GET':
        return jsonify(lordOfTheList)

# ? *** Driver ***
if __name__ == "__main__":
    app.run(debug=True)
