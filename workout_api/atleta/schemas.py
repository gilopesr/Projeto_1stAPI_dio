from typing import Annotated, Optional
from pydantic import Field, PositiveFloat

from workout_api.contrib.schemas import BaseSchema, OutMixin

class Atleta(BaseSchema):
    nome: Annotated[str, Field(description='Nome do atleta', example= 'julia', max_length=50)]
    cpf: Annotated[str, Field(description='CPF do atleta', example= '123456789', max_length=11)]
    idade: Annotated[int, Field(description='Idade do atleta', example= '20')]
    peso: Annotated[PositiveFloat, Field(description='peso do atleta', example= '81.6')]
    altura: Annotated[PositiveFloat, Field(description='altura do atleta', example= '1.84')]
    sexo: Annotated[str, Field(description='sexo do atleta', example= 'F', max_length=1)]

class AtletaIn(Atleta):
    pass
class AtletaOut(Atleta, OutMixin):
    pass
class AtletaUpdate(BaseSchema):
    nome: Annotated[Optional[str], Field(None, description='Nome do atleta', example='Joao', max_length=50)]
    idade: Annotated[Optional[int], Field(None, description='Idade do atleta', example=25)]