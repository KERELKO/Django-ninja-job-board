from ninja import Schema

from src.apps.profiles.entities.profiles import (
    EmployerProfile as EmployerProfileEntity,
)


class BaseEmployerProfileSchema(Schema):
    first_name: str
    last_name: str
    email: str
    company_name: str = ''


class EmployerProfileOut(BaseEmployerProfileSchema):
    id: int

    @staticmethod
    def from_entity(entity: EmployerProfileEntity) -> 'EmployerProfileOut':
        return EmployerProfileOut(**entity.to_dict())


class EmployerProfileIn(BaseEmployerProfileSchema):
    user_id: int


class EmployerProfileUpdate(BaseEmployerProfileSchema):
    ...