import fastapi
from fastapi_chameleon import template
from viewmodels.home.indexviewmodel import IndexViewModel
from starlette.requests import Request

router = fastapi.APIRouter()


@router.get("/")
@template()
def index(request: Request):
    vm = IndexViewModel(request)
    return vm.to_dict()


@router.get("/about")
@template()
def about():
    return {}
