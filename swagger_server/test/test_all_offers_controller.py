# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.request_all_offers import RequestAllOffers  # noqa: E501
from swagger_server.models.response_all_offers import ResponseAllOffers  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAllOffersController(BaseTestCase):
    """AllOffersController integration test stubs"""

    def test_all_offers(self):
        """Test case for all_offers

        Todas las ofertas.
        """
        body = RequestAllOffers()
        response = self.client.open(
            '/offers',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
