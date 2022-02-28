from typing import Callable

import requests
from colorama import Fore
from environs import Env
from faker import Faker
from pytest import fixture
from requests.models import Response

Env().read_env()


@fixture
def host():
    return 'http://localhost:5000'


@fixture
def colorized() -> Callable[[str], str]:
    ''' Retorna uma função anônima que adiciona informações de cor a uma\n
        string para melhor visualização no terminal. Retorna a seguinte função::

            colorized(msg: str) -> str

        Exemplo::

            def test_if_get_route_returns_correct_status_code(colorized):

                resp = requests.get(...)

                err_msg = "Status code errado!"

                assert resp.status_code == 200, colorized(err_msg) '''
    return lambda msg: f'{Fore.CYAN}{msg}{Fore.RESET}'


@fixture
def fake() -> Faker:
    ''' Retorna uma instância do objeto `faker.Faker`

        Exemplo::

            def test_if_create_route_returns_correct_status_code(fake):
                payload = {
                    "name": fake.name(),
                    "email": fake.email(),
                    "password": fake.password(),
                    "description": fake.text(),
                }

                resp = post("/users", payload)

                err_msg = "Status code errado!"

                assert resp.status_code == 201, err_msg '''
    return Faker()


@fixture
def post(host) -> Callable[[str, dict], Response]:
    ''' Constrói uma requisição de `POST`. Retorna a seguinte função::

                post(endpoint: str, payload: dict, headers: dict) -> Response

            Parâmetros:

            `endpoint` - sufixo da base URL. Deve começar com uma barra `/`

            `payload` - objeto JSON a ser enviado na requisição

            `headers` - dicionário contendo as informações de headers. O\n
                padrão é `None`

            Exemplo::

                def test_if_create_route_returns_correct_status_code(post):
                    payload = {...}

                    resp = post("/users", payload)

                    err_msg = "Status code errado!"

                    assert resp.status_code == 201, err_msg '''
    return lambda endpoint, payload, headers:\
        requests.post(f'{host}{endpoint}', json=payload, headers=headers)


@fixture
def get(host) -> Callable[[str, dict], Response]:
    ''' Constrói uma requisição de `GET`. Retorna a seguinte função::

                get(endpoint: str, headers: dict) -> Response

            Parâmetros:

            `endpoint` - sufixo da base URL. Deve começar com uma barra `/`

            `headers` - dicionário contendo as informações de headers. O\n
                padrão é `None`

            Exemplo::

                def test_if_get_route_returns_correct_payload(get):
                    payload = {...}
                    token = ...
                    headers = {"Authorization": f"Bearer {token}"}

                    expected = {...}

                    resp = get("/tattoos", headers)

                    err_msg = "Resposta errada!"

                    assert resp.json() == expected, err_msg '''
    return lambda endpoint, headers:\
        requests.get(f'{host}{endpoint}', headers=headers)


@fixture
def patch(host) -> Callable[[str, dict], Response]:
    ''' Constrói uma requisição de `PATCH`. Retorna a seguinte função::

                patch(endpoint: str, payload: dict, headers: dict) -> Response

            Parâmetros:

            `endpoint` - sufixo da base URL. Deve começar com uma barra `/`

            `payload` - objeto JSON a ser enviado na requisição

            `headers` - dicionário contendo as informações de headers. O\n
                padrão é `None`

            Exemplo::

                def test_if_update_route_returns_correct_status_code(patch):
                    payload = {...}
                    token = ...
                    headers = {"Authorization": f"Bearer {token}"}

                    resp = patch("/tattoos", payload, headers)

                    err_msg = "Status code errado!"

                    assert resp.status_code == 200, err_msg '''
    return lambda endpoint, payload, headers:\
        requests.patch(f'{host}{endpoint}', json=payload, headers=headers)


@fixture
def delete(host) -> Callable[[str, dict], Response]:
    ''' Constrói uma requisição de `DELETE`. Retorna a seguinte função::

                delete(endpoint: str, headers: dict) -> Response

            Parâmetros:

            `endpoint` - sufixo da base URL. Deve começar com uma barra `/`

            `headers` - dicionário contendo as informações de headers. O\n
                padrão é `None`

            Exemplo::

                def test_if_delete_route_returns_correct_status_code(delete):
                    token = ...
                    headers = {"Authorization": f"Bearer {token}"}

                    resp = delete("/tattoos", headers)

                    err_msg = "Status code errado!"

                    assert resp.status_code == 204, err_msg '''
    return lambda endpoint, headers:\
        requests.delete(f'{host}{endpoint}', headers=headers)
