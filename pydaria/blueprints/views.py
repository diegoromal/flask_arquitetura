from flask import abort, render_template
from pydaria.models.products import Products


def init_app(app):
    @app.route("/")
    def index():
        products = Products.query.all()
        return render_template("index.html", products=products)

    @app.route("/product/<product_id>/")
    def product(product_id):
        product = Products.query.filter_by(id=product_id).first() or abort(
            404, "Produto não encontrado"
        )
        return render_template("product.html", product=product)
