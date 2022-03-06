import fastapi
import os
from database.digest_gen import Digest
from fastapi_chameleon import template
from fastapi import Form


router = fastapi.APIRouter()


@router.get("/template")
async def html_static():
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


@router.get('/template/index')
@template(template_file='index.pt')
async def index_template():
    from random import randint
    count = randint(1, 20)
    # faker info
    from faker import Faker
    fake_info = Faker("pl-PL")
    password = Digest()
    username = fake_info.name()
    return {
        "user_name": username,
        "user_list": [{"name": f"{fake_info.name()} - {fake_info.address()}", "chrome": fake_info.chrome(),
                       "link": "https://abixedukacja.eu"}
                      for _ in range(count)],  # lista słowników
        "passwd_hash": password.generate(),
        "tech_spec": os.uname(),
    }


# POST form via /static file
# http://127.0.0.1:8000/static/post-form.html


#  RuntimeError: Form data requires "python-multipart" to be installed.
@router.post("/template/post")
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
