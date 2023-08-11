# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.request_get_single_offer import RequestGetSingleOffer  # noqa: E501
from swagger_server.models.response_get_single_offer import ResponseGetSingleOffer  # noqa: E501
from swagger_server.test import BaseTestCase


class TestGetSingleOfferController(BaseTestCase):
    """GetSingleOfferController integration test stubs"""

    def test_get_single_offer(self):
        """Test case for get_single_offer

        Obtener una oferta específica.
        """
        body = RequestGetSingleOffer()
        response = self.client.open(
            '/getOffer',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
