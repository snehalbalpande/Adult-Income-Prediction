from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return "this is income prediction ML project"
       


if __name__=="__main__":
   app.run()