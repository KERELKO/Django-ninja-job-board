from abc import abstractmethod

from src.apps.profiles.entities.jobseekers import JobSeekerEntity
from src.apps.vacancies.entities import VacancyEntity
from src.common.services.base import BaseService


class BaseVacancyService(BaseService):
    @abstractmethod
    def create(self, employer_id: int, **vacancy_data) -> VacancyEntity: ...

    @abstractmethod
    def add_candidate(self, candidate_id: int, vacancy_id: int) -> None: ...

    @abstractmethod
    def get_list_candidates(
        self,
        vacancy_id: int,
        offset: int,
        limit: int,
    ) -> list[JobSeekerEntity]: ...
