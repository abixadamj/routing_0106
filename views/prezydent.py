import fastapi
from fastapi import Form
from fastapi_chameleon import template

router = fastapi.APIRouter()

@router.post("/templates/prezydent", tags=["templates", "prezydent"])
@template(template_file='prezydent.pt')
async def read_data_form_prezydent(email: str = Form(...),
                         html_prezydent: str = Form(...),
                         ):
    from bs4 import BeautifulSoup

    html_data = BeautifulSoup(html_prezydent,  'html.parser')
    linki_raw = [ link.get("href") for link in html_data.find_all("a") ]
    linki_ok = []
    for element in linki_raw:
        if not element.startswith("https://prezydent.pl"):
            element = "https://prezydent.pl" + element
        linki_ok.append(element)


    return {"email": email, "strona": str(html_data.title.string),
            "linki": linki_ok,
           }
