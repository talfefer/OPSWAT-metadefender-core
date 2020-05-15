# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.dlp_response_dlp_info_hits_ccn import DLPResponseDlpInfoHitsCcn
from openapi_server import util

from openapi_server.models.dlp_response_dlp_info_hits_ccn import DLPResponseDlpInfoHitsCcn  # noqa: E501

class DLPResponseDlpInfoHits(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, ccn=None):  # noqa: E501
        """DLPResponseDlpInfoHits - a model defined in OpenAPI

        :param ccn: The ccn of this DLPResponseDlpInfoHits.  # noqa: E501
        :type ccn: DLPResponseDlpInfoHitsCcn
        """
        self.openapi_types = {
            'ccn': DLPResponseDlpInfoHitsCcn
        }

        self.attribute_map = {
            'ccn': 'ccn'
        }

        self._ccn = ccn

    @classmethod
    def from_dict(cls, dikt) -> 'DLPResponseDlpInfoHits':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DLPResponse_dlp_info_hits of this DLPResponseDlpInfoHits.  # noqa: E501
        :rtype: DLPResponseDlpInfoHits
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ccn(self):
        """Gets the ccn of this DLPResponseDlpInfoHits.


        :return: The ccn of this DLPResponseDlpInfoHits.
        :rtype: DLPResponseDlpInfoHitsCcn
        """
        return self._ccn

    @ccn.setter
    def ccn(self, ccn):
        """Sets the ccn of this DLPResponseDlpInfoHits.


        :param ccn: The ccn of this DLPResponseDlpInfoHits.
        :type ccn: DLPResponseDlpInfoHitsCcn
        """

        self._ccn = ccn
