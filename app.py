
from flask import Flask, render_template, redirect, request
import time
from threading import Thread
from toggleWifi import toggleWifi

app = Flask(__name__)

@app.route("/", methods=['GET'])
def page():
    return render_template('./index.html')

@app.route("/", methods=['POST'])
def process_post():
    def do_work():
        toggleWifi(False)
        print("turning wifi off")
        time.sleep(60)
        toggleWifi(True)
    
    toggle = request.form.get("toggle")
    if (toggle):
        print("turning off wifi")
        thread = Thread(target=do_work)
        thread.start()

    return redirect("/")