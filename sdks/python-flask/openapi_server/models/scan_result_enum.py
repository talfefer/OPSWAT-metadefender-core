# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class ScanResultEnum(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    _0 = "0"
    _1 = "1"
    _2 = "2"
    _3 = "3"
    _4 = "4"
    def __init__(self):  # noqa: E501
        """ScanResultEnum - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'ScanResultEnum':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ScanResultEnum of this ScanResultEnum.  # noqa: E501
        :rtype: ScanResultEnum
        """
        return util.deserialize_model(dikt, cls)
