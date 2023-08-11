# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.request_offer_data import RequestOfferData  # noqa: F401,E501
from swagger_server import util


class RequestNewOffer(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, channel: str=None, external_transaction_id: str=None, data: RequestOfferData=None):  # noqa: E501
        """RequestNewOffer - a model defined in Swagger

        :param channel: The channel of this RequestNewOffer.  # noqa: E501
        :type channel: str
        :param external_transaction_id: The external_transaction_id of this RequestNewOffer.  # noqa: E501
        :type external_transaction_id: str
        :param data: The data of this RequestNewOffer.  # noqa: E501
        :type data: RequestOfferData
        """
        self.swagger_types = {
            'channel': str,
            'external_transaction_id': str,
            'data': RequestOfferData
        }

        self.attribute_map = {
            'channel': 'channel',
            'external_transaction_id': 'externalTransactionId',
            'data': 'data'
        }
        self._channel = channel
        self._external_transaction_id = external_transaction_id
        self._data = data

    @classmethod
    def from_dict(cls, dikt) -> 'RequestNewOffer':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RequestNewOffer of this RequestNewOffer.  # noqa: E501
        :rtype: RequestNewOffer
        """
        return util.deserialize_model(dikt, cls)

    @property
    def channel(self) -> str:
        """Gets the channel of this RequestNewOffer.


        :return: The channel of this RequestNewOffer.
        :rtype: str
        """
        return self._channel

    @channel.setter
    def channel(self, channel: str):
        """Sets the channel of this RequestNewOffer.


        :param channel: The channel of this RequestNewOffer.
        :type channel: str
        """

        self._channel = channel

    @property
    def external_transaction_id(self) -> str:
        """Gets the external_transaction_id of this RequestNewOffer.


        :return: The external_transaction_id of this RequestNewOffer.
        :rtype: str
        """
        return self._external_transaction_id

    @external_transaction_id.setter
    def external_transaction_id(self, external_transaction_id: str):
        """Sets the external_transaction_id of this RequestNewOffer.


        :param external_transaction_id: The external_transaction_id of this RequestNewOffer.
        :type external_transaction_id: str
        """

        self._external_transaction_id = external_transaction_id

    @property
    def data(self) -> RequestOfferData:
        """Gets the data of this RequestNewOffer.


        :return: The data of this RequestNewOffer.
        :rtype: RequestOfferData
        """
        return self._data

    @data.setter
    def data(self, data: RequestOfferData):
        """Sets the data of this RequestNewOffer.


        :param data: The data of this RequestNewOffer.
        :type data: RequestOfferData
        """

        self._data = data
