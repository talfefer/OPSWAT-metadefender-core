# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class InlineResponse20010(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, max_file_size=None, name=None):  # noqa: E501
        """InlineResponse20010 - a model defined in OpenAPI

        :param max_file_size: The max_file_size of this InlineResponse20010.  # noqa: E501
        :type max_file_size: int
        :param name: The name of this InlineResponse20010.  # noqa: E501
        :type name: str
        """
        self.openapi_types = {
            'max_file_size': int,
            'name': str
        }

        self.attribute_map = {
            'max_file_size': 'max_file_size',
            'name': 'name'
        }

        self._max_file_size = max_file_size
        self._name = name

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse20010':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_10 of this InlineResponse20010.  # noqa: E501
        :rtype: InlineResponse20010
        """
        return util.deserialize_model(dikt, cls)

    @property
    def max_file_size(self):
        """Gets the max_file_size of this InlineResponse20010.

        The maximum allowed file size (in bytes) for this rule.  # noqa: E501

        :return: The max_file_size of this InlineResponse20010.
        :rtype: int
        """
        return self._max_file_size

    @max_file_size.setter
    def max_file_size(self, max_file_size):
        """Sets the max_file_size of this InlineResponse20010.

        The maximum allowed file size (in bytes) for this rule.  # noqa: E501

        :param max_file_size: The max_file_size of this InlineResponse20010.
        :type max_file_size: int
        """

        self._max_file_size = max_file_size

    @property
    def name(self):
        """Gets the name of this InlineResponse20010.

        A unique identifier for identify in the used rule for a scan..  # noqa: E501

        :return: The name of this InlineResponse20010.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse20010.

        A unique identifier for identify in the used rule for a scan..  # noqa: E501

        :param name: The name of this InlineResponse20010.
        :type name: str
        """

        self._name = name
