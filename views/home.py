import fastapi
from fastapi_chameleon import template

router = fastapi.APIRouter()

@router.get('/')
@template(template_file='index.html') #this brings in the html file
async def index(user: str = 'anon'):
    return {
            'user_name': user
    }


@router.get('/')
async def about():
    return {}
