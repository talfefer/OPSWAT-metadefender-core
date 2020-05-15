# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class InlineObject2(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, old_password=None, new_password=None):  # noqa: E501
        """InlineObject2 - a model defined in OpenAPI

        :param old_password: The old_password of this InlineObject2.  # noqa: E501
        :type old_password: str
        :param new_password: The new_password of this InlineObject2.  # noqa: E501
        :type new_password: str
        """
        self.openapi_types = {
            'old_password': str,
            'new_password': str
        }

        self.attribute_map = {
            'old_password': 'old_password',
            'new_password': 'new_password'
        }

        self._old_password = old_password
        self._new_password = new_password

    @classmethod
    def from_dict(cls, dikt) -> 'InlineObject2':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_object_2 of this InlineObject2.  # noqa: E501
        :rtype: InlineObject2
        """
        return util.deserialize_model(dikt, cls)

    @property
    def old_password(self):
        """Gets the old_password of this InlineObject2.

        The current password in plain text  # noqa: E501

        :return: The old_password of this InlineObject2.
        :rtype: str
        """
        return self._old_password

    @old_password.setter
    def old_password(self, old_password):
        """Sets the old_password of this InlineObject2.

        The current password in plain text  # noqa: E501

        :param old_password: The old_password of this InlineObject2.
        :type old_password: str
        """

        self._old_password = old_password

    @property
    def new_password(self):
        """Gets the new_password of this InlineObject2.

        The new password in plain text  # noqa: E501

        :return: The new_password of this InlineObject2.
        :rtype: str
        """
        return self._new_password

    @new_password.setter
    def new_password(self, new_password):
        """Sets the new_password of this InlineObject2.

        The new password in plain text  # noqa: E501

        :param new_password: The new_password of this InlineObject2.
        :type new_password: str
        """

        self._new_password = new_password
