from dataclasses import dataclass
from logging import Logger
from typing import Iterable
from django.db.models import Q

from src.apps.profiles.converters.employers import ORMEmployerConverter
from src.apps.profiles.entities.employers import EmployerEntity
from src.apps.profiles.models.employers import EmployerProfile
from src.apps.profiles.filters import EmployerFilter
from src.common.services.exceptions import ServiceException

from .base import BaseEmployerService


@dataclass
class ORMEmployerService(BaseEmployerService):
    logger: Logger
    converter: ORMEmployerConverter = ORMEmployerConverter()

    def _get_model_or_raise_exception(
        self,
        message: str = None,
        related: bool = False,
        **lookup_parameters,
    ) -> EmployerProfile:
        try:
            if related:
                profile = EmployerProfile.objects.select_related('user').get(
                    **lookup_parameters
                )
            else:
                profile = EmployerProfile.objects.get(**lookup_parameters)
        except EmployerProfile.DoesNotExist:
            self.logger.info(
                'Profile not found',
                extra={'info': lookup_parameters},
            )
            if not message:
                raise ServiceException(message='Profile not found')
            raise ServiceException(message=message)
        return profile

    def _build_queryset(self, filters: EmployerFilter) -> Q:
        query = Q()
        if filters.company_name:
            query &= Q(company_name=filters.company_name)
        return query

    def get_list(
        self, filters: EmployerFilter, offset: int, limit: int
    ) -> list[EmployerEntity]:
        query = self._build_queryset(filters)
        employers = EmployerProfile.objects.filter(query)[
            offset:offset+limit
        ]
        return [self.converter.handle(employer) for employer in employers]

    def get_total_count(self, filters: EmployerFilter) -> list[EmployerEntity]:
        query = self._build_queryset(filters)
        total_count = EmployerProfile.objects.filter(query).count()
        return total_count

    def get_all(self, filters: EmployerFilter) -> Iterable[EmployerEntity]:
        query = self._build_queryset(filters)
        for employer in EmployerProfile.objects.filter(query):
            yield employer

    def get(self, id: int) -> EmployerEntity | None:
        try:
            employer = EmployerProfile.objects.get(id=id)
        except EmployerProfile.DoesNotExist:
            raise ServiceException('profile not found')
        return self.converter.handle(employer)
