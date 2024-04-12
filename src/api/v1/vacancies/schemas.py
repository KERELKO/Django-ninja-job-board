from datetime import datetime

from src.apps.vacancies.entities import Vacancy as VacancyEntity
from src.api.schemas import BaseSchema


class BaseVacancySchema(BaseSchema):
    ...


class VacancyIn(BaseVacancySchema):
    title: str
    description: str
    company_name: str
    location: str | None = None
    remote: bool | None = None
    required_experience: int = 0


class VacancyOut(BaseVacancySchema):
    id: int
    title: str
    description: str
    slug: str
    open: bool
    company_name: str
    created_at: datetime
    remote: bool | None = None
    location: str | None = None
    required_experience: int = 0

    @staticmethod
    def from_entity(entity: VacancyEntity) -> 'VacancyOut':
        return VacancyOut(
            id=entity.id,
            title=entity.title,
            description=entity.description,
            slug=entity.slug,
            open=entity.open,
            company_name=entity.company_name,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
            location=entity.location,
            required_experience=entity.required_experience,
            remote=entity.remote,
        )
