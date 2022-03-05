import uvicorn
from fastapi import FastAPI, responses
from starlette.staticfiles import StaticFiles

from views import komputery
from views import inne
from views import api_responses_test
from emails import get_email
from database import cookies

app = FastAPI()

# dodamy: https://fastapi.tiangolo.com/tutorial/body/

def configure_routers():
    app.include_router(komputery.router)
    app.include_router(inne.router)
    app.include_router(api_responses_test.router)
    app.include_router(get_email.router)
    app.include_router(cookies.router)
    app.mount('/static', StaticFiles(directory='static'), name='static')


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get('/favicon.ico')
def get_favicon():
    return responses.RedirectResponse(url='static/img/favicon.ico')


if __name__ == '__main__':
    configure_routers()
    uvicorn.run(app, port=8000, host='127.0.0.1')
