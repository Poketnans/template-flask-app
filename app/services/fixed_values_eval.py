from werkzeug.exceptions import BadRequest


def fixed_values_eval(data: dict, **kwargs) -> None:
    ''' Avalia no payload os campos que possuem valores fixos.

            `data` - o payload recebido

            `kwargs` - os campos que possuem valor fixo. Recebem como valor a\n
                lista de valores possíveis.

        Exemplo::

            fixed_values_eval(
                data=payload,
                tag=['Success', 'Fail', 'Waiting']
            )

        Exceções:
            `werkzeug.exceptions.BadRequest` - Algum campo veio com valor não\n
                permitido
    '''

    invalid_types = {
        key: data[key]
        for key, fixed_values in kwargs.items()
        if data[key] not in fixed_values
    }

    resp = {
        "msg": {
            "valid_options": kwargs,
            "recieved_options": {
                key: data[key]
                for key, _ in kwargs.items()
            }
        }
    }

    if invalid_types:
        raise BadRequest(resp)
