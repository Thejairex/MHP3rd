from flask import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/item-shop")
def item_shop():
    return render_template("item-shop.html")

if __name__ == "__main__":
    app.run(debug=True)