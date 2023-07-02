from dataclasses import dataclass, field

from flask import Blueprint
from flask import render_template

products_app = Blueprint(
    "products_app",
    __name__,
    url_prefix="/products",
)

@dataclass
class Product:
    id: int
    name: str

@dataclass
class ProductsStorage:
    last_id: int = 0
    products: dict[int, Product] = field(default_factory=list)

    @property
    def next_id(self):
        self.last_id += 1
        return self.last_id

    def add_product(self, name: str):
        product = Product(id=self.next_id,name=name)
        self.products[product.id] = product

    def get_all_products(self) -> list[Product]:
        return list(self.products.values())

    def get_product_by_id(self.product_id: int) -> Product | None:
        return self.products.get(product_id)



@products_app.get("/", endpoint="list")
def get_products_list():
    products: list[Product] = storage.get_all_products()
    return  render_template("list.html", products=products)
