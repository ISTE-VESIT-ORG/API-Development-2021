from flask import Flask, render_template, request
from flask.json import jsonify
from flask.wrappers import Request

# * Flask constructor takes the name of current module (__name__) as argument.
app = Flask(__name__)

# ! -------------------- GLOBAL VARIABLES START --------------------
# demo for JSON
agents = {
    "sova": {
        "real name": "Hunter",
        "abilities": ["recon bolt", "shock bolt", "owl drone"],
        "ulitmate": ["hunter's fury"]
    },
    "cypher": {
        "real name": "Aamir",
        "abilities": ["trap wire", "spycam", "cybercage"],
        "ulitmate": ["neural theft"]
    },
    "reyna": {
        "real name": "Delilah",
        "abilities": ["heal", "dismiss", "leer"],
        "ulitmate": ["Empress"]
    }
}

# demo list
weapons = ['Operator', 'Vandal']

# ! -------------------- GLOBAL VARIABLES END --------------------

# ? *** Base route ***
# * The route() function of the Flask class is a decorator 
# * it tells the application which URL should call the associated function.
@app.route('/')
def home():
    name = "Aamir"

    # render_template is used to render a HTML page
    # it looks for HTML files in `templates folder`
    # we can send variables to template using the syntax below
    return render_template('home.html', name=name);

# ? *** GET request ***
# ? Get agents
@app.route('/getAgents', methods=['GET'])
def getAgents():
    if request.method == 'GET':
        return jsonify(agents)
    else:
        return "PLZ send GET request :("

# ? Get weapons
@app.route('/getWeapons', methods=['GET'])
def getWeapons():
    if request.method == 'GET':
        return jsonify(weapons)
    else:
        return "PLZ send GET request :("

# ? *** POST request ***
# ? Insert weapons in the list
@app.route('/addWeopens/<string:weaponName>', methods=['POST'])
def addWeopens(weaponName):
    if request.method == 'POST':
        weapons.append(weaponName)
        return "Data is inserted !!"

# ? *** DELETE ***
# ? Delete weapon from the list
@app.route('/deleteWeapon/<string:weaponName>', methods=['DELETE'])
def deleteWeapon(weaponName):
    if request.method == 'DELETE':
        print(weapons)
        if weaponName in weapons:
            weapons.remove(weaponName)
            return "Weapon is removed"
        else:
            return "That weapon is not there in the list"


# ? *** Driver function ***
if __name__ == "__main__":
    app.run(debug=True)
