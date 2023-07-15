from flask import *
from werkzeug.utils import secure_filename
from security import Security

from db import Db

app = Flask(__name__)
db = Db()

def upload(folder, archivo):
    if archivo:
        filename = secure_filename(archivo.filename)
        
        if Security().verify_extension(filename):
            url = f"img/{folder}/{filename}"
            print(url)
            archivo.save("static/" + url)
            return url
        
        else:
            return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/item-shop")
def item_shop():
    datas = db.select_all("Items_Shop")
    return render_template("item-shop.html", datas=datas)

@app.route("/item-shop/add")
def form_add_item_shop():
    return render_template("add_item_shop.html")

@app.route("/api/add_item_shop", methods=["POST"])
def add_item_shop():
    file = request.files['image']
    url = upload("objetos", file)
    if url:
        name = request.form["name"]
        description = request.form["description"]
        price = request.form["price"]
        shop_level = request.form["shop_level"]
        
        db.insert("Items_Shop", (name, description, price, shop_level, url))
    return redirect(url_for("index"))



if __name__ == "__main__":
    app.run(debug=True)