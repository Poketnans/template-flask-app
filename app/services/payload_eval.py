from app.errors import FieldMissingError, InvalidValueTypesError


def payload_eval(data: dict, optional: list, **kwargs) -> dict:
    ''' Avalia o payload em existência, opcionalidade e tipo de campo. Retorna\n
        um dicionário contendo os campos que foram informados como argumentos\n
        nomeados, ou seja, ignora os campos excedentes.

            `data` - o payload recebido

            `optional` - lista com os nomes dos campos opcionais

            `kwargs` - campos possíveis para a requisição. Seus valores\n
                correspondem ao tipo de dado permitido para aquele campo.

        Todos os campos permitidos à requisição devem ser passados como\n
        argumentos nomeados, recebendo como valor os tipo correspondente::

            payload_eval(
                data=payload,
                name=str,
                price=float,
                description=str,
                opitonal=['description'],
            )

        Exceções:
            `app.errors.FieldMissingError` - Campo obrigatório não informado.\n
        Se o campo não fornecido estiver na lista de opcionais, a exceção mão\n
        é levantada.

            `app.errors.InvalidValueTypesError` - Há campos cujo tipo não\n
        não coresponde ao informado nos argumentos nomeados.
        '''
    missing_keys = [
        key
        for key in kwargs.keys()
        if key not in data.keys()
    ]

    if set(missing_keys).difference(optional):
        msg = {"error": f"missing keys: {missing_keys}"}
        raise FieldMissingError(description=msg)

    invalid_types = {
        "error":
        f"Invalid type, `{field_name}` type should be {value_type} but was {type(data[field_name])}"
        for field_name, value_type in kwargs.items()
        if field_name in data.keys()
        if type(data[field_name]) != value_type
    }

    if invalid_types:
        raise InvalidValueTypesError(description=invalid_types)

    return {key: data[key] for key in kwargs.keys() if key in data.keys()}
