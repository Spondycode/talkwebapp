import fastapi
import uvicorn
from fastapi_chameleon import template
import fastapi_chameleon
from views import home
from views import account
from views import packages


app = fastapi.FastAPI()

# This had to be added to let the app know where the templates are.
fastapi_chameleon.global_init('templates')

@app.get('/')
@template(template_file='index.html')
def index(user: str = 'anon'):
    return {
        'user_name': user
    }

app.include_router(home.router)
app.include_router(account.router)
app.include_router(packages.router)


# This will be replaced later when deployed to the internet.
# It is the python way to say run directly
if __name__ == '__main__':
    uvicorn.run(app)
