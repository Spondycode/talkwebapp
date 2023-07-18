import fastapi
from fastapi.requests import Request
from fastapi_chameleon import template
from viewmodels.account.register_viewmodel import RegisterViewModel
from viewmodels.account.account_viewmodel import AccountViewModel
from viewmodels.account.login_viewmodel import LoginViewModel

router = fastapi.APIRouter()


@router.get("/account")
def index(request: fastapi.Request):
    vm = AccountViewModel(request)
    return {}


@router.get("/account/register")
def register(request: Request):
    vm = RegisterViewModel(request)
    return {}


@router.get("/account/login")
def login(request: Request):
    vm = LoginViewModel(request)
    return {}


@router.get("/account/logout")
def logout(request: Request):
    vm = LogoutViewModel(request)
    return {}
