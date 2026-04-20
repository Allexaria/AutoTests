from pydantic import BaseModel


class ProductsListResponse(BaseModel):
    products: list[dict]
