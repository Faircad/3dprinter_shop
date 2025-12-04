from flask import Flask, render_template

app = Flask(__name__)

# -------------------------
# Главные страницы
# -------------------------

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


# -------------------------
# Каталог (главная страница каталога)
# -------------------------

@app.route("/catalog")
def catalog():
    return render_template("catalog.html")


# -------------------------
# Разделы каталога
# -------------------------

@app.route("/catalog/fdm")
def catalog_fdm():
    return render_template("catalog_fdm.html")

@app.route("/catalog/budget")
def catalog_budget():
    return render_template("catalog_budget.html")

@app.route("/catalog/pro")
def catalog_pro():
    return render_template("catalog_pro.html")

@app.route("/catalog/materials")
def catalog_materials():
    return render_template("catalog_materials.html")

@app.route("/catalog/parts")
def catalog_parts():
    return render_template("catalog_parts.html")

@app.route("/catalog/service")
def catalog_service():
    return render_template("catalog_service.html")

@app.route("/blog")
def catalog_blog():
    return render_template("catalog_blog.html")


# -------------------------
# Страницы товаров — базовые модели
# -------------------------

@app.route("/product/a1pro")
def product_a1pro():
    return render_template("product_a1pro.html")

@app.route("/product/a1max")
def product_a1max():
    return render_template("product_a1max.html")

@app.route("/product/ultracorex")
def product_ultracorex():
    return render_template("product_ultracorex.html")

@app.route("/product/studiomini")
def product_studiomini():
    return render_template("product_studiomini.html")


# -------------------------
# Страницы товаров — профессиональные модели
# -------------------------

@app.route("/product/titanforge_x500")
def product_titanforge_x500():
    return render_template("product_titanforge_x500.html")

@app.route("/product/proline_m330")
def product_proline_m330():
    return render_template("product_proline_m330.html")

@app.route("/product/industroprint_s240")
def product_industroprint_s240():
    return render_template("product_industroprint_s240.html")


# -------------------------
# Запуск сервера
# -------------------------

if __name__ == "__main__":
    app.run(debug=True)
