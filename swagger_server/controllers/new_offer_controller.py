import connexion
import six

from swagger_server.models.request_new_offer import RequestNewOffer  # noqa: E501
from swagger_server.models.response_new_offer import ResponseNewOffer  # noqa: E501
from swagger_server import util


def new_offer(body=None):  # noqa: E501
    """Crear una nueva oferta.

    Crear una nueva oferta. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: ResponseNewOffer
    """
    if connexion.request.is_json:
        body = RequestNewOffer.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
