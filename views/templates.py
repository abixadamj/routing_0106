import fastapi
from fastapi_chameleon import template
from database.digest_gen import Digest
import os

router = fastapi.APIRouter()


@router.get("/templates/first", tags=["templates"])
async def templates_first():
    html = """
        <!DOCTYPE html>
    <html lang="pl">
    <head>
        <meta charset="UTF-8">
        <title>Simple page</title>
    </head>
    <body>
      <h3>Hello world! Nothing More.</h3>
    </body>
    </html>
        """
    return fastapi.responses.HTMLResponse(content=html)

@router.get("/templates/second", tags=["templates"])
@template(template_file='test.pt')
async def second_template():
    return {
        "user": "Adam",
        "password": "Hasełko",
    }

@router.get("/templates/third", tags=["templates"])
@template(template_file='bootstrap_first.pt')
async def third_template():
    dig = Digest()
    return {
        "user": "Adam",
        "password": "Hasełko",
        "tech_spec": os.uname(),  # Linux and Mac only !!!
        "digest": dig.generate(),
    }