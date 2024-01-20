from flask import Flask

app = Flask("MaWebapp")

@app.route("/")
def accueil():
  return "coucou"

app.run("0.0.0.0", 3904)