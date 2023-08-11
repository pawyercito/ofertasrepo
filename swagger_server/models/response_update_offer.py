# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.offer_data import OfferData  # noqa: F401,E501
from swagger_server import util


class ResponseUpdateOffer(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, code: str=None, message: str=None, internal_transaction_id: str=None, external_transaction_id: str=None, data: OfferData=None):  # noqa: E501
        """ResponseUpdateOffer - a model defined in Swagger

        :param code: The code of this ResponseUpdateOffer.  # noqa: E501
        :type code: str
        :param message: The message of this ResponseUpdateOffer.  # noqa: E501
        :type message: str
        :param internal_transaction_id: The internal_transaction_id of this ResponseUpdateOffer.  # noqa: E501
        :type internal_transaction_id: str
        :param external_transaction_id: The external_transaction_id of this ResponseUpdateOffer.  # noqa: E501
        :type external_transaction_id: str
        :param data: The data of this ResponseUpdateOffer.  # noqa: E501
        :type data: OfferData
        """
        self.swagger_types = {
            'code': str,
            'message': str,
            'internal_transaction_id': str,
            'external_transaction_id': str,
            'data': OfferData
        }

        self.attribute_map = {
            'code': 'code',
            'message': 'message',
            'internal_transaction_id': 'internalTransactionId',
            'external_transaction_id': 'externalTransactionId',
            'data': 'data'
        }
        self._code = code
        self._message = message
        self._internal_transaction_id = internal_transaction_id
        self._external_transaction_id = external_transaction_id
        self._data = data

    @classmethod
    def from_dict(cls, dikt) -> 'ResponseUpdateOffer':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ResponseUpdateOffer of this ResponseUpdateOffer.  # noqa: E501
        :rtype: ResponseUpdateOffer
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self) -> str:
        """Gets the code of this ResponseUpdateOffer.


        :return: The code of this ResponseUpdateOffer.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code: str):
        """Sets the code of this ResponseUpdateOffer.


        :param code: The code of this ResponseUpdateOffer.
        :type code: str
        """

        self._code = code

    @property
    def message(self) -> str:
        """Gets the message of this ResponseUpdateOffer.


        :return: The message of this ResponseUpdateOffer.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """Sets the message of this ResponseUpdateOffer.


        :param message: The message of this ResponseUpdateOffer.
        :type message: str
        """

        self._message = message

    @property
    def internal_transaction_id(self) -> str:
        """Gets the internal_transaction_id of this ResponseUpdateOffer.


        :return: The internal_transaction_id of this ResponseUpdateOffer.
        :rtype: str
        """
        return self._internal_transaction_id

    @internal_transaction_id.setter
    def internal_transaction_id(self, internal_transaction_id: str):
        """Sets the internal_transaction_id of this ResponseUpdateOffer.


        :param internal_transaction_id: The internal_transaction_id of this ResponseUpdateOffer.
        :type internal_transaction_id: str
        """

        self._internal_transaction_id = internal_transaction_id

    @property
    def external_transaction_id(self) -> str:
        """Gets the external_transaction_id of this ResponseUpdateOffer.


        :return: The external_transaction_id of this ResponseUpdateOffer.
        :rtype: str
        """
        return self._external_transaction_id

    @external_transaction_id.setter
    def external_transaction_id(self, external_transaction_id: str):
        """Sets the external_transaction_id of this ResponseUpdateOffer.


        :param external_transaction_id: The external_transaction_id of this ResponseUpdateOffer.
        :type external_transaction_id: str
        """

        self._external_transaction_id = external_transaction_id

    @property
    def data(self) -> OfferData:
        """Gets the data of this ResponseUpdateOffer.


        :return: The data of this ResponseUpdateOffer.
        :rtype: OfferData
        """
        return self._data

    @data.setter
    def data(self, data: OfferData):
        """Sets the data of this ResponseUpdateOffer.


        :param data: The data of this ResponseUpdateOffer.
        :type data: OfferData
        """

        self._data = data