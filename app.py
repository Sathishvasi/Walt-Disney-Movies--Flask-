from flask import Flask, render_template
from data import Datas
from upcomingData import UpcomingDatas

app = Flask(__name__)

Datas = Datas()
Upcoming = UpcomingDatas()

@app.route("/")
def index():
    return render_template('home.html')

@app.route("/upcoming")
def upcoming():
    return render_template('upcoming.html', movies = Upcoming)

@app.route("/movies")
def movies():
    return render_template('movies.html', movies = Datas)

if __name__ == '__main__':
    app.run(debug=True)