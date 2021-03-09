from flask import Flask, render_template, redirect
from random import randint
from threading import Thread
from os import environ

from requests import get

# # # # # # # # # # # # # # # # # # # # 

app = Flask("Fellow Hashbrown APIs")
imgur_hashes = {
    "2021": {
        "January": "GZgoSdg",
        "February": "jVLIRE7",
        "March": "N7Rcvsj"
    }
}
imgur_images = {}

# # # # # # # # # # # # # # # # # # # # 

@app.errorhandler(Exception)
def error(error):
    return render_template("error.html")

@app.route("/")
def home():
    
    # Go through each of the months in each year
    #   to move the image links into the dictionary
    for year in imgur_hashes:

        # If the year does not exist in the images yet, create it
        if year not in imgur_images:
            imgur_images[year] = {}
        
        # Iterate through the months in the hashes
        for month in imgur_hashes[year]:

            # If the month does not exist in the images yet, create it
            if month not in imgur_images[year]:
                imgur_images[year][month] = []
            
            # Load the imgur album's images, if there are any
            if imgur_hashes[year][month] is not None:
                images = get(
                    "https://api.imgur.com/3/album/{}/images".format(
                        imgur_hashes[year][month]),
                    headers = {
                        "Authorization": "Client-ID {}".format(environ["IMGUR_API_KEY"])
                    }
                ).json()["data"]
                for i in range(len(images)):
                    images[i] = {
                        "link": images[i]["link"],
                        "description": images[i]["description"],
                        "type": images[i]["type"]
                    }
                imgur_images[year][month] = images
            else:
                imgur_images[year][month] = None
    
    return render_template(
        "astronomy.html",
        years = imgur_images
    )

@app.route("/favicon")
@app.route("/favicon.ico")
def favicon():
    return redirect("/static/favicon.ico"), 302

# # # # # # # # # # # # # # # # # # # # 

def run():
    app.run(
        host = '0.0.0.0', 
        port = randint(1025, 9999))

t = Thread(target = run)
t.start()
