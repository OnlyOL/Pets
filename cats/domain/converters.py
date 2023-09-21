from cats.models import Cat

from .entities import *


# noinspection PyTypeChecker
class UserEntityConverter:
    @classmethod
    def to_entity(cls, orm_object: Cat) -> CatsEntity:
        return CatsEntity(
            cat_id=orm_object.pk,
            name=orm_object.name,
            breed=orm_object.breed,
            age=orm_object.age,
            color=orm_object.color,
            is_neutered=orm_object.is_neutered,
            owner=orm_object.owner
        )
