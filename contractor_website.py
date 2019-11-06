from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
from functools import reduce
import os

app = Flask(__name__)

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/contractor_website_db')
client = MongoClient(host=f"{host}?retryWrites=false")
db = client.get_default_database()

space_suits = db.suits

# missions = [
#     {
#         "Name":"Mars",
#         "Time":"asdfasf",
#         "Terrain":"asdfadf",
#         "Volatility":"n/10",
#         "Life":"No"
#     },
#     {
#         "Name":"Earth",
#         "Time":"asdfasf",
#         "Terrain":"asdfadf",
#         "Volatility":"n/10",
#         "Life":"Human"
#     }
# ]
#
# products =[
#     {
#         "Type":"SpaceSuit",
#         "Name":"Jumpman",
#         "Price":"out of this world",
#         "Specs":"anti-gravity kit, flexible materials"
#     },
#     {
#         "Type":"Spacesuit",
#         "Name":"Lil' Pinch",
#         "Price":"underground",
#         "Specs":"power claws, weight distribution"
#     }
# ]


#
#
#
# @app.route("/mission")
# def mission():
#     return render_template('mission.html')
#
# @app.route("/products")
# def products():
#     return render_template('products.html')
#



@app.route('/')
def index():
    """Return homepage."""
    return render_template('index.html', suits=space_suits.find())


@app.route('/new')
def new_suit():
    """Return new suit creation page."""
    return render_template('new_suit.html')

@app.route('/new', methods=['POST'])
def create_suit():
    """Make a new suit posting according to user's specifications."""
    suit = {
        'name': request.form.get('name'),
        'price': request.form.get('price'),
        'img_url': request.form.get('img_url')
    }
    suit_id = space_suits.insert_one(suit).inserted_id
    return redirect(url_for('show_suit', suit_id=suit_id))

@app.route('/suit/<suit_id>')
def show_suit(suit_id):
    """Show a single suit."""
    suit = space_suits.find_one({'_id': ObjectId(suit_id)})
    return render_template('show_suit.html', suit=suit)

@app.route('/edit/<suit_id>', methods=['POST'])
def update_suit(suit_id):
    """Edit a suit posting."""
    new_suit = {
        'name': request.form.get('name'),
        'price': request.form.get('price'),
        'img_url': request.form.get('img_url')
    }
    space_suits.update_one(
        {'_id': ObjectId(suit_id)},
        {'$set': new_suit}
    )
    return redirect(url_for('show_suit', suit_id=suit_id))

@app.route('/delete/<suit_id>', methods=['POST'])
def delete_suit(suit_id):
    """Delete a suit."""
    space_suits.delete_one({'_id': ObjectId(suit_id)})
    return redirect(url_for('index'))

@app.route('/edit/<suit_id>', methods=['GET'])
def edit_suit(suit_id):
    """Page to submit an edit on a suit."""
    suit = space_suits.find_one({'_id': ObjectId(suit_id)})
    return render_template('edit_suit.html', suit=suit)

@app.route('/login')
def login_page():
    """Return new suit creation page."""
    return render_template('login.html')

@app.route('/login')
def login_page():
    """Return new suit creation page."""
    return render_template('login.html')

@app.route('/login')
def login_page():
    """Return new suit creation page."""
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
