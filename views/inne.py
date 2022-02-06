import fastapi

router = fastapi.APIRouter()


@router.get("/others")
async def others():
    """To jest opis mojej funkcji - będzie ciekawie.
    A tutaj kolejna linia mojego opisu.
    I jeszcze jedna.
    Koniec."""
    return {"message": "Others"}