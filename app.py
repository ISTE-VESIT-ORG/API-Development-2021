from flask import *
import random

app = Flask(__name__)

nameList = []
lordOfTheList = []
colors = []

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
        funnyTitles = ["Great", "Conquerer", "Magician", "Evolver","Depressed","Racist","Connoisseur","Adaptable","Adventurous","Amarous","diligent","Humble","Courageous","Efficient","Enchanting","Generous","Magnetic","Likeable","Sincere","Non","Trustworthy","Resourceful","Wellread","Wise","Zealous","Resilient","Reliable","Determined","Strong","Stupendous","Exceptional","Generous","Kind","Persuasive","Vivacious","Witty","Extraordinary","Divine","Breathtaking","Flawless","Magnificent","Lively","Versatile","Amazing","Funloving","Welltravelled","Outgoing","amicable","Friendly","Perseverant","Enthusiastic","Affectionate","Thoughtful","Modest","Hygienic","Considerate","Courteous"]
        title = funnyTitles[random.randint(0, len(funnyTitles)-1)]
        someString += " The "+title

        # Insert the new item in list
        lordOfTheList.insert(0, someString)
        colors.insert(0,random.randint(0,6))
        
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
        return jsonify(lordOfTheList, colors)

# ? *** Driver ***
if __name__ == "__main__":
    app.run(debug=True)
