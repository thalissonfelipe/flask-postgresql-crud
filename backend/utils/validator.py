from utils.errors import BadRequestException


def validate_create_body(body: dict) -> None:
    user_fields = ['name', 'age', 'address']
    for field in user_fields:
        if field not in body:
            raise BadRequestException(f'Missing {field} parameter.')

    if (
        not isinstance(body['name'], str)
        or not isinstance(body['age'], int)
        or not isinstance(body['address'], dict)
    ):
        raise BadRequestException('Invalid JSON.')

    address_fields = ['street', 'number', 'city', 'state']
    for field in address_fields:
        if field not in body['address']:
            raise BadRequestException(f'Missing address.{field} parameter.')

    if (
        not isinstance(body['address']['street'], str)
        or not isinstance(body['address']['number'], int)
        or not isinstance(body['address']['city'], str)
        or not isinstance(body['address']['state'], str)
    ):
        raise BadRequestException('Invalid JSON.')


def validate_update_body(body: dict) -> None:
    print(body)
    if (
        'name' in body and not isinstance(body['name'], str)
        or 'age' in body and not isinstance(body['age'], int)
        or 'address' in body and not isinstance(body['address'], dict)
    ):
        raise BadRequestException('Invalid JSON.')

    if 'address' in body:
        address = body['address']
        if (
            'street' in address and not isinstance(address['street'], str)
            or 'number' in address and not isinstance(address['number'], int)
            or 'city' in address and not isinstance(address['city'], str)
            or 'state' in address and not isinstance(address['state'], str)
        ):
            raise BadRequestException('Invalid JSON.')
