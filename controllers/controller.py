from flask import render_template
from app import app
from models.player import *
from models.game import *

@app.route("/")
def welcome():
    return render_template("welcome.html", title="Home")


@app.route("/play")
def index():
    return render_template("index.html", title="Home")

@app.route("/<choice_1>/<choice_2>")
def display_result(choice_1, choice_2):
    player_1=Player("Calum", choice_1)
    player_2=Player("Tony", choice_2)
    game=Game(player_1, player_2)
    winner= game.get_results(choice_1,choice_2)
    return render_template("results.html", title="Results", winner=winner )

@app.route("/<choice_1>")
def player_1_choice(choice_1):
    return render_template("player2_choice.html", title="choice_2", choice_1=choice_1)




