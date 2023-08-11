# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.request_update_offer import RequestUpdateOffer  # noqa: E501
from swagger_server.models.response_update_offer import ResponseUpdateOffer  # noqa: E501
from swagger_server.test import BaseTestCase


class TestUpdateOfferController(BaseTestCase):
    """UpdateOfferController integration test stubs"""

    def test_update_offer(self):
        """Test case for update_offer

        Actualizar oferta.
        """
        body = RequestUpdateOffer()
        response = self.client.open(
            '/offers/{id_offer}'.format(id_offer=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
