from typing import Optional

from pydantic import BaseModel as SCBaseModel

class CursoSchemaCreate(SCBaseModel):
    title: str
    number_of_classes: int
    hours: int


class CursoSchema(SCBaseModel):
    id: Optional[int]
    title: str
    number_of_classes: int
    hours: int

    class Config:
        from_attributes = True

class CursoSchemaUpdate(SCBaseModel):
    title: str
    number_of_classes: int
    hours: int
