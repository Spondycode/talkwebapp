import fastapi
from fastapi_chameleon import template
from starlette import requests
from starlette.requests import Request

from viewmodels.home.indexviewmodel import IndexViewModel

router = fastapi.APIRouter()


@router.get("/")
@template()
def index(request: Request):
    vm = IndexViewModel(request)
    return vm.to_dict()
