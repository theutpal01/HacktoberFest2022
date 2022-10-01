from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "At your service, sir!"

def run():
  app.run(host='0.0.0.0',port=8080)

def alivek():
    t = Thread(target=run)
    t.start()