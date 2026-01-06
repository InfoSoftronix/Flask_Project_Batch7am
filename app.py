from flask import Flask
app=Flask(__name__) # Flask(__main__)  Creating a Instance for Flask Class 

@app.route("/")
def home():
    return "<h1> Welcome to Flask </h1>"

@app.route("/index")
def index():
    return "<h1> Welcome to Flask In Softronix IT Training...</h1>"

@app.route("/soft")
def soft():
    return " <marquee> <h1> Softronix IT Training...</h1> </marquee>"

if __name__ == '__main__':
    app.run(debug=True)