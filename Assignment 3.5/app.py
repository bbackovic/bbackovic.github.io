  
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def start():
    title = "To Karaoke or Not to Karaoke"
    
    text = """It a nice summer night and your friends are calling you to go out. However, you are working on your dream app!"""

    choices = [
        ('enter_house',"Karaoke with friends"),
        ('run_away',"Build your dream app")
    ]

    return render_template('adventure.html', title=title, text=text, choices=choices)



@app.route("/inside")
def enter_house():
    title = "Your friends are super happy"
    
    text = """... now you have to pick a song"""

    choices = [
        ('up_stairs',"Shallow"),
        ('run_away',"This was a mistake")
    ]

    return render_template('adventure.html', title=title, text=text, choices=choices)

@app.route("/stairs")
def up_stairs():
    title = "Oh no, that type of a night!"
    
    text = """Is Adele up next?"""

    choices = []

    return render_template('adventure.html', title=title, text=text, choices=choices)

@app.route("/escape")
def run_away():
    title = "Great job!"
    
    text = """You crack a beer open and start working on the front-end"""

    choices = []

    return render_template('adventure.html', title=title, text=text, choices=choices)



