import connexion
import six

from swagger_server.models.request_update_offer import RequestUpdateOffer  # noqa: E501
from swagger_server.models.response_update_offer import ResponseUpdateOffer  # noqa: E501
from swagger_server import util


def update_offer(id_offer, body=None):  # noqa: E501
    """Actualizar oferta.

    Actualizar oferta. # noqa: E501

    :param id_offer: 
    :type id_offer: int
    :param body: 
    :type body: dict | bytes

    :rtype: ResponseUpdateOffer
    """
    if connexion.request.is_json:
        body = RequestUpdateOffer.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
