
from flask import Flask, render_template, redirect, request
import time
from threading import Thread
from toggle_wifi import toggle_wifi

app = Flask(__name__)

@app.route("/", methods=['GET'])
def page():
    return render_template('./index.html')

@app.route("/", methods=['POST'])
def process_post():
    toggle = request.form.get("toggle")
    toggle = int(toggle)
    
    def do_work():
        # toggle_wifi(False)
        print("turning wifi off for ", toggle * 60)
        time.sleep(toggle * 60)
        # toggle_wifi(True)
    
    
    if (toggle):
        print("turning off wifi")
        thread = Thread(target=do_work)
        thread.start()

    return redirect("/")