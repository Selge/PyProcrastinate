from datetime import datetime
from flask import Flask, render_template
import requests
import json


app = Flask(__name__)


def get_meme():
    url = "https://meme-api.com/gimme"
    response = json.loads(requests.request("GET", url).text)
    meme_large = response["preview"][-1]
    return meme_large


def your_local_time():
    date = datetime.now().date()
    time = datetime.now().strftime('%H:%M')
    return date, time


@app.route('/')
def index():
    meme_pic = get_meme()
    date, time = your_local_time()
    return render_template("meme_index.html", meme_pic=meme_pic, date=date, time=time)


if __name__ == '__main__':
    app.run()
