from django.http import HttpRequest
from ninja import Query, Router
from ninja.security import django_auth_superuser

from src.api.schemas import APIResponseSchema, ListPaginatedResponse
from src.api.v1.profiles.employers.schemas import EmployerProfileOut
from src.apps.profiles.filters import EmployerFilter
from src.apps.profiles.services.base import BaseEmployerService
from src.common.container import Container
from src.common.filters.pagination import PaginationIn, PaginationOut

router = Router(tags=['employers'])


@router.get(
    '',
    auth=django_auth_superuser,
    response=APIResponseSchema[ListPaginatedResponse[EmployerProfileOut]],
)
def get_employer_list(
    request: HttpRequest,
    filters: Query[EmployerFilter],
    pagination_in: Query[PaginationIn],
) -> APIResponseSchema[ListPaginatedResponse[EmployerProfileOut]]:
    service = Container.resolve(BaseEmployerService)
    profile_list = service.get_list(
        filters=filters,
        offset=pagination_in.offset,
        limit=pagination_in.limit,
    )
    profile_count = service.get_total_count(filters=filters)
    pg_out = PaginationOut(
        offset=pagination_in.offset,
        limit=pagination_in.limit,
        total=profile_count,
    )
    data = ListPaginatedResponse(
        items=[EmployerProfileOut.from_entity(p) for p in profile_list],
        pagination=pg_out,
    )
    response = APIResponseSchema(data=data)
    return response
