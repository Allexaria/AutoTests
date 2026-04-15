class CatalogService:
    def __init__(self, client):
        self.client = client

    def get_products_list(self):
        return self.client.get("/productsList")

    def post_products_list(self):
        return self.client.post("/productsList", json={})

    def get_brands_list(self):
        return self.client.get("/brandsList")

    def put_brands_list(self):
        return self.client.put("/brandsList")

    def search_product(self, search_product):
        return self.client.post("/searchProduct", data={"search_product": search_product})

    def search_product_without_param(self):
        return self.client.post("/searchProduct")
