from swagger_server.utils.logs.logging import log as logging
import requests

from requests import ConnectTimeout


def get_request(internal_transaction_id, external_transaction_id, base_url, endpoint, method, headers, data,
                payload=None):
    """Genera request swagger_client

    Args:
        base_url (string): base_url
        endpoint (string) : endpoint
        method (string) : method tipo get, post, put, delete, etc.
        headers (string): headers
        data (string) : body del request
        payload (string): payload - parameters
        tiempo de espera de la solicitud 30 segundo para conectarse y 30 segundos para leer la solicitud.
    Returns:
        object: objeto response
    """
    msg_log = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: %r '

    try:
        log = logging()
        url = f"{base_url}{endpoint}"
        log.info(msg_log, internal_transaction_id, external_transaction_id, "get_request", __name__, "inicio consumo de reqquest")
        
        response = requests.request(method, url, headers=headers, json=data, params=payload, timeout=(30, 30))
        log.info(msg_log, internal_transaction_id, external_transaction_id, "get_request", __name__, "fin consumo de reqquest")

        message = f"ejecucion request baseurl: {base_url} method: {method} status_code:{response.status_code}"
        function_name = "get_request"
        package_name = __name__
        log.info(msg_log, internal_transaction_id, external_transaction_id, function_name, package_name, message)

        return response
    except ConnectTimeout:
        message = f"error en la ejecucion request baseurl: {base_url} method: {method}"
        function_name = "get_request"
        package_name = __name__
        log = logging()
        log.critical(msg_log, internal_transaction_id, external_transaction_id, function_name, package_name, message)

    except Exception as ex:
        message = f"ejecucion request baseurl: {base_url} method: {method} exception: {ex}"
        function_name = "get_request"
        package_name = __name__
        log = logging()
        log.critical(msg_log, internal_transaction_id, external_transaction_id, function_name, package_name, message)


def get_form_request(internal_transaction_id, external_transaction_id, base_url, endpoint, method, headers, data,
                payload=None):
    """Genera request swagger_client

    Args:
        base_url (string): base_url
        endpoint (string) : endpoint
        method (string) : method tipo get, post, put, delete, etc.
        headers (string): headers
        data (string) : body del request
        payload (string): payload - parameters
        tiempo de espera de la solicitud 30 segundo para conectarse y 30 segundos para leer la solicitud.
    Returns:
        object: objeto response
    """
    msg_log = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: %r '

    try:

        url = f"{base_url}{endpoint}"
        response = requests.request(method, url, headers=headers, params=payload, timeout=(30, 30), data=data)

        message = f"ejecucion request baseurl: {base_url} method: {method} status_code:{response.status_code}"
        function_name = "get_form_request"
        package_name = __name__
        log = logging()
        log.info(msg_log, internal_transaction_id, external_transaction_id, function_name, package_name, message)

        return response
    except ConnectTimeout:
        message = f"error en la ejecucion request baseurl: {base_url} method: {method}"
        function_name = "get_form_request"
        package_name = __name__
        log = logging()
        log.critical(msg_log, internal_transaction_id, external_transaction_id, function_name, package_name, message)

    except Exception as ex:
        message = f"ejecucion request baseurl: {base_url} method: {method} exception: {ex}"
        function_name = "get_form_request"
        package_name = __name__
        log = logging()
        log.critical(msg_log, internal_transaction_id, external_transaction_id, function_name, package_name, message)
