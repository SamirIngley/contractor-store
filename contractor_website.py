from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
#from bson.object_id import ObjectId

app = Flask(__name__)

missions = [
    {
        "Name":"Mars",
        "Time":"asdfasf",
        "Terrain":"asdfadf",
        "Volatility":"n/10",
        "Life":"No"
    },
    {
        "Name":"Earth",
        "Time":"asdfasf",
        "Terrain":"asdfadf",
        "Volatility":"n/10",
        "Life":"Human"
    }
]

products =[
    {
        "Type":"SpaceSuit",
        "Name":"Jumpman",
        "Price":"out of this world",
        "Specs":"anti-gravity kit, flexible materials"
    },
    {
        "Type":"Spacesuit",
        "Name":"Lil' Pinch",
        "Price":"underground",
        "Specs":"power claws, weight distribution"
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/mission")
def mission():
    return render_template('mission.html', products=products)


if __name__ == '__main__':
    app.run(debug=True)
