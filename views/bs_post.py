import fastapi
from fastapi import Form

router = fastapi.APIRouter()

@router.post("/yandex/html", tags=["yandex"])
async def read_data_yandex(yandex_html: str = Form(...)):
    from bs4 import BeautifulSoup
    html_data = BeautifulSoup(yandex_html, "html5lib")  # 'html.parser')
    print(html_data)
    link_dict = {}
    href = html_data.find_all('a')
    print(href)
    for id, link in enumerate(href):
        link_dict[id] = link.get('href')
    return link_dict