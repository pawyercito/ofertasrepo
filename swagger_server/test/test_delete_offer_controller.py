# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.response_delete_offer import ResponseDeleteOffer  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDeleteOfferController(BaseTestCase):
    """DeleteOfferController integration test stubs"""

    def test_delete_offer(self):
        """Test case for delete_offer

        Eliminar oferta.
        """
        response = self.client.open(
            '/offers/{id_offer}'.format(id_offer=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
