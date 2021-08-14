from typing import List

from fastapi import APIRouter, Depends
from flashcards_core.schedulers import get_available_schedulers

from flashcards_server.api import oauth2_scheme


router = APIRouter(
    prefix="/algorithms",
    tags=["algorithms"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[str])
def get_algorithms(
    offset: int = 0, limit: int = 100, token: str = Depends(oauth2_scheme)
):
    return get_available_schedulers()