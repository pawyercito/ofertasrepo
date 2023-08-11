import connexion
import six

from swagger_server.models.request_get_single_offer import RequestGetSingleOffer  # noqa: E501
from swagger_server.models.response_get_single_offer import ResponseGetSingleOffer  # noqa: E501
from swagger_server import util


def get_single_offer(body=None):  # noqa: E501
    """Obtener una oferta específica.

    Obtener una oferta específica. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: ResponseGetSingleOffer
    """
    if connexion.request.is_json:
        body = RequestGetSingleOffer.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
