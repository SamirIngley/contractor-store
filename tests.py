from unittest import TestCase, main as unittest_main, mock
from bson.objectid import ObjectId
from app import app

sample_playlist_id = ObjectId('5d55cffc4a3d4031f42827a3')

products =[
    {
        "Name":"Jumpman",
        "Price":"2000000",
        "IMG URL":"anti-gravity kit, flexible materials"
    },
    {
        "Type":"Spacesuit",
        "Name":"Lil' Pinch",
        "Price":"underground",
        "Specs":"power claws, weight distribution"
    }
]
