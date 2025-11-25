from typing import List

from fastapi import APIRouter
from fastapi import status
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.curso_model import CursoModel

from schemas.curso_schema import CursoSchema
from schemas.curso_schema import CursoSchemaCreate
from schemas.curso_schema import CursoSchemaUpdate

from core.deps import get_session

router = APIRouter()

# Adicionar um novo curso
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=CursoSchema)
async def post_curso(curso: CursoSchemaCreate, db: AsyncSession = Depends(get_session)):
    novo_curso = CursoModel(
        title=curso.title,
        number_of_classes=curso.number_of_classes,
        hours=curso.hours
    )

    db.add(novo_curso)
    await db.commit()
    await db.refresh(novo_curso)

    return novo_curso


# Listar todos os cursos
@router.get('/', response_model=List[CursoSchema])
async def get_cursos(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CursoModel)
        result = await session.execute(query)
        cursos: List[CursoModel] = result.scalars().all()

        return cursos
    
# Listar um curso pelo ID
@router.get('/{curso_id}', response_model=CursoSchema, status_code=status.HTTP_200_OK)
async def get_curso(curso_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CursoModel).filter(CursoModel.id == curso_id)
        result = await session.execute(query)
        curso = result.scalar_one_or_none()

        if curso:
            return curso
        else:
            raise HTTPException(detail='Curso não encontrado', status_code=status.HTTP_404_NOT_FOUND)
        

# Atualizar um curso pelo ID
@router.put('/{curso_id}', response_model=CursoSchema, status_code=status.HTTP_200_OK)
async def put_curso(curso_id: int, curso: CursoSchemaUpdate, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CursoModel).filter(CursoModel.id == curso_id)
        result = await session.execute(query)
        curso_up: CursoModel = result.scalar_one_or_none()

        if curso_up:
            curso_up.title = curso.title
            curso_up.number_of_classes = curso.number_of_classes
            curso_up.hours = curso.hours

            await session.commit()
            await session.refresh(curso_up)

            return curso_up
        else:
            raise HTTPException(detail='Curso não encontrado', status_code=status.HTTP_404_NOT_FOUND)

        

# Deletar um curso pelo ID
@router.delete('/{curso_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_curso(curso_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CursoModel).filter(CursoModel.id == curso_id)
        result = await session.execute(query)
        curso_del: CursoModel = result.scalar_one_or_none()

        if curso_del:
            await session.delete(curso_del)
            await session.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail='Curso não encontrado', status_code=status.HTTP_404_NOT_FOUND)