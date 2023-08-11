import connexion
import six

from swagger_server.models.response_delete_offer import ResponseDeleteOffer  # noqa: E501
from swagger_server import util


def delete_offer(id_offer):  # noqa: E501
    """Eliminar oferta.

    Eliminar una oferta existente. # noqa: E501

    :param id_offer: 
    :type id_offer: int

    :rtype: ResponseDeleteOffer
    """
    return 'do some magic!'
