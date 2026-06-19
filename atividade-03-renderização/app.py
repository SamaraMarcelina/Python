from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def curriculo():
    return render_template("index.html", nome="Samara Marcelina")

@app.route("/cotemig")
def cotemig():
    return render_template("index.html", nome="Samara Marcelina - Cotemig")

if __name__ == "__main__":
    app.run(debug=True)