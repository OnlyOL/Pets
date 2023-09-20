from typing import Optional
from cats.models import Cat


class CatsDAO:

    @classmethod
    def create_cat(
            cls,
            cat_id: int,
            name: str,
            breed: str,
            age: int,
            color: str,
            is_neutered: bool,
            owner: int,

    ):
        cat = Cat.objects.create(
            cat_id=cat_id,
            name=name,
            breed=breed,
            age=age,
            color=color,
            is_neutered=is_neutered,
            owner=owner,
        )
        return cat
