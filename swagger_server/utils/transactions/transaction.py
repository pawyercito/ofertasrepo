import uuid


def generate_internal_transaction_id():

    """Script para generar el id de la transacción del microservicio (UUID objects according to RFC 4122)

    Returns:
        string: id interno de la transacción
    """
    return uuid.uuid4()