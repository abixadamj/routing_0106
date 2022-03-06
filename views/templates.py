import fastapi
import os
from fastapi_chameleon import template
from database.digest_gen import Digest
from fastapi import Form

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


@router.get('/templates/fake_data', tags=["templates"])
@template(template_file='fake_data.pt')
async def index_template():
    from random import randint
    count = randint(1, 200)
    # faker info
    from faker import Faker
    fake_info = Faker(["ru-RU", "it-IT", "jp-JP"])
    password = Digest()
    username = fake_info.name()
    return {
        "user_name": username,
        "user_list": [{"name": f"{fake_info.name()} - {fake_info.address()}",
                       "chrome": fake_info.chrome(),
                       "link": "https://abixedukacja.eu"}
                      for _ in range(count)],  # lista słowników
        "passwd_hash": password.generate(),
        "tech_spec": os.uname(),
    }


#  RuntimeError: Form data requires "python-multipart" to be installed.
@router.post("/templates/post", tags=["templates"])
async def read_data_form(auth_id: str = Form(...),
                         password: str = Form(...),
                         email: str = Form(...),
                         big_text: str = Form(...),
                         ):
    from database.digest_gen import Digest
    security = Digest()
    return {"id": auth_id, "pass": password,
            "email": email, "digest": security.generate(),
            "text": big_text}
