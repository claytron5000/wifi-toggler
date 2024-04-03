
from flask import Flask, render_template, redirect, request, send_from_directory
from threading import Thread
from toggle_wifi import toggle_wifi2

app = Flask(__name__)

@app.route("/", methods=['GET'])
def page():
    return render_template('./index.html')

@app.route('/static/<path:path>')
def send_static(path):
    print("get static")
    return send_from_directory('./static', path)

@app.route("/", methods=['POST'])
def process_post():
    toggle = request.form.get("toggle")
    toggle = int(toggle)
    
    def do_work():
        toggle_wifi2(toggle)
        # print("turning wifi off for ", toggle * 60)
        # time.sleep(toggle * 60)
        # toggle_wifi(True)
    
    
    if (toggle):
        print("turning off wifi")
        thread = Thread(target=do_work)
        thread.start()

    return redirect("/")