# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.request_new_offer import RequestNewOffer  # noqa: E501
from swagger_server.models.response_new_offer import ResponseNewOffer  # noqa: E501
from swagger_server.test import BaseTestCase


class TestNewOfferController(BaseTestCase):
    """NewOfferController integration test stubs"""

    def test_new_offer(self):
        """Test case for new_offer

        Crear una nueva oferta.
        """
        body = RequestNewOffer()
        response = self.client.open(
            '/newOffer',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
