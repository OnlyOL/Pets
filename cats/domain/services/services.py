from typing import Optional
from cats.domain.daos import CatsDAO


class CatsService:
    def __int__(self):
        self.cat_dao = CatsDAO()

    def create_cat(
            self,
            name: str,
            breed: str,
            age: int,
            color: str,
            is_neutered: bool,
            owner: int,
    ):
        return self.cat_dao.create_cat(
            name,
            breed,
            age,
            color,
            is_neutered,
            owner,
        )
