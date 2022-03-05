import fastapi
from fastapi.responses import RedirectResponse
from fastapi import Response, Request, status
from database.digest_gen import Digest

router = fastapi.APIRouter()


ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 60 + 120  # in seconds


@router.get("/cookies/set", tags=["cookies"])
async def cookies_test_get():
    response = RedirectResponse(url="/static/first.html")
    digest = Digest()
    secret_key = digest.generate()
    print(f"Gen: {secret_key}")
    response.set_cookie(
        "TEST",
        value=secret_key,
        domain="127.0.0.1",  # different -> Error
        httponly=False,
        max_age=ACCESS_TOKEN_EXPIRE_MINUTES,
        expires=ACCESS_TOKEN_EXPIRE_MINUTES,
    )
    return response


@router.put("/cookies/set", tags=["cookies"])
async def cookies_test_put():
    response = Response()
    digest = Digest()
    secret_key = digest.generate()
    print(f"PUT Gen: {secret_key}")
    response.set_cookie(
        "TEST_PUT",
        value=secret_key,
        domain="127.0.0.1",  # different -> Error
        httponly=False,
        max_age=ACCESS_TOKEN_EXPIRE_MINUTES,
        expires=ACCESS_TOKEN_EXPIRE_MINUTES,
    )
    return response


@router.get("/cookies/list", tags=["cookies"])
async def cookies_list_get(request: Request, response: Response):
    cookies = request.cookies.items()
    if not cookies:
        print("No cookies")
        response.status_code = status.HTTP_202_ACCEPTED
        # poniższe nie pokazuje zwróconych danych
        # response.status_code = status.HTTP_204_NO_CONTENT
        return {"Error": "No cookies!"}
    for cookie in cookies:
        print(cookie)
        print(f"Key: {cookie[0]}")
        print(f"VAL: {cookie[1]}")
    return cookies


@router.delete("/cookies/del", tags=["cookies"])
async def cookies_del_del(request: Request):
    cookies = request.cookies.items()
    response = Response()
    if not cookies:
        print("No cookies - no delete")
        response.status_code = status.HTTP_204_NO_CONTENT
        return response
    for cookie in cookies:
        print(f"DELETE: {cookie}")
        response.delete_cookie(cookie[0])  # , max_age=0, expires=0, domain="127.0.0.1")
    return response
