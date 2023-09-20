from typing import Optional
from .services import CatsService


class CreateCatUseCase:
    def __int__(self):
        self.cat_service = CatsService()

    def execute(
            self,
            cat_id: int,
            name: str,
            breed: str,
            age: int,
            color: str,
            is_neutered: bool,
            owner: int,
    ):
        cat = self.cat_service.create_cat(
            cat_id,
            name,
            breed,
            age,
            color,
            is_neutered,
            owner,
        )
        return cat
