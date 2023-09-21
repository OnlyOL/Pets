from typing import Optional
from .services import CatsService


class CreateCatUseCase:
    def __int__(self):
        self.cat_service = CatsService()

    def execute(
            self,
            name: str,
            breed: str,
            age: int,
            color: str,
            is_neutered: bool,
            owner: int,
    ):
        errors = []
        cat = self.cat_service.create_cat(
            name,
            breed,
            age,
            color,
            is_neutered,
            owner,
        )
        return cat


class UpdateCatUseCase:
    def __int__(self):
        self.cat_service = CatsService()

    def execute(self, cat):
        return cat

class DeleteCatUseCase:
    def __int__(self):
        self.cat_service = CatsService()

    def execute(self, cat):
        return cat
