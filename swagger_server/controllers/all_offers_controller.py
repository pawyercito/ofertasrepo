import connexion
import six

from swagger_server.models.request_all_offers import RequestAllOffers  # noqa: E501
from swagger_server.models.response_all_offers import ResponseAllOffers  # noqa: E501
from swagger_server import util


def all_offers(body=None):  # noqa: E501
    """Todas las ofertas.

    Todas las ofertas # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: ResponseAllOffers
    """
    if connexion.request.is_json:
        body = RequestAllOffers.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
