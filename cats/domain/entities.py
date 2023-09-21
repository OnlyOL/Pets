from dataclasses import dataclass
from typing import Optional


class BaseEntity:
    pass


@dataclass
class CatsEntity(BaseEntity):
    cat_id: int
    name: str
    breed: str
    age: int
    color: str
    is_neutered: bool
    owner: int
