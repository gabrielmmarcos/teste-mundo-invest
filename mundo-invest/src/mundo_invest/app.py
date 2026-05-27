from http import HTTPStatus

from fastapi import FastAPI

from mundo_invest.models.models import Cliente

app = FastAPI()


@app.get("/", status_code=HTTPStatus.OK)
def read_root():
    return list(Cliente)
