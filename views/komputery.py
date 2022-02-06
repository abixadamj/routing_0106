import fastapi

router = fastapi.APIRouter()

computers = {
    "Sharp MZ-700": [1998, 750, "Zilog Z-80"],
    "PC XT": [2001, 500, "Intel 8080"],
    "PC AT": [2004, 550, "Intel 386DX"],
    "PC NEW": [2018, 1000, "Intel Core i5"]
}


@router.get("/computers_all")
async def computers_all():
    """Wyświetla wszystkie komputery"""
    all_computers_id = computers.keys()
    return {"message": "All computers",
            "all id": f"{all_computers_id}"}

@router.get("/computer_id/{computer_id}")
async def computer_info(computer_id: str, count: int = 1):
    if computer_id in computers:
        computer_info = computers[computer_id]
        price_value = f"Price for {count} computers will be {count * computer_info[1]} USD."
        return {
            "Computer id": computer_id,
            "production year": computer_info[0],
            "price in USD": computer_info[1],
            "CPU name": computer_info[2],
            "price": price_value,
        }
    else:
        computer_info = f"There is no computer like: {computer_id}"

        return {
            "Computer id": computer_id,
            "info": computer_info
        }

@router.get("/computer_id_b/{computer_id}/{count}")
async def computer_info(computer_id: str, count: int):
    if computer_id in computers:
        computer_info = computers[computer_id]
        price_value = f"Price for {count} computers will be {count * computer_info[1]} USD."
        return {
            "Computer id": computer_id,
            "production year": computer_info[0],
            "price in USD": computer_info[1],
            "CPU name": computer_info[2],
            "price": price_value,
        }
    else:
        computer_info = f"There is no computer like: {computer_id}"

        return {
            "Computer id": computer_id,
            "info": computer_info
        }
