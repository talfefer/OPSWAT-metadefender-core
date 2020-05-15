# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.admin_config_update_disabledupdate import AdminConfigUpdateDisabledupdate
from openapi_server import util

from openapi_server.models.admin_config_update_disabledupdate import AdminConfigUpdateDisabledupdate  # noqa: E501

class AdminConfigUpdate(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, autoupdateperiod=None, deleteafterimport=None, disabledupdate=None, pickupfolder=None, source=None):  # noqa: E501
        """AdminConfigUpdate - a model defined in OpenAPI

        :param autoupdateperiod: The autoupdateperiod of this AdminConfigUpdate.  # noqa: E501
        :type autoupdateperiod: int
        :param deleteafterimport: The deleteafterimport of this AdminConfigUpdate.  # noqa: E501
        :type deleteafterimport: bool
        :param disabledupdate: The disabledupdate of this AdminConfigUpdate.  # noqa: E501
        :type disabledupdate: List[AdminConfigUpdateDisabledupdate]
        :param pickupfolder: The pickupfolder of this AdminConfigUpdate.  # noqa: E501
        :type pickupfolder: str
        :param source: The source of this AdminConfigUpdate.  # noqa: E501
        :type source: str
        """
        self.openapi_types = {
            'autoupdateperiod': int,
            'deleteafterimport': bool,
            'disabledupdate': List[AdminConfigUpdateDisabledupdate],
            'pickupfolder': str,
            'source': str
        }

        self.attribute_map = {
            'autoupdateperiod': 'autoupdateperiod',
            'deleteafterimport': 'deleteafterimport',
            'disabledupdate': 'disabledupdate',
            'pickupfolder': 'pickupfolder',
            'source': 'source'
        }

        self._autoupdateperiod = autoupdateperiod
        self._deleteafterimport = deleteafterimport
        self._disabledupdate = disabledupdate
        self._pickupfolder = pickupfolder
        self._source = source

    @classmethod
    def from_dict(cls, dikt) -> 'AdminConfigUpdate':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AdminConfigUpdate of this AdminConfigUpdate.  # noqa: E501
        :rtype: AdminConfigUpdate
        """
        return util.deserialize_model(dikt, cls)

    @property
    def autoupdateperiod(self):
        """Gets the autoupdateperiod of this AdminConfigUpdate.

        The interval (in minutes) for checking for new updates.  # noqa: E501

        :return: The autoupdateperiod of this AdminConfigUpdate.
        :rtype: int
        """
        return self._autoupdateperiod

    @autoupdateperiod.setter
    def autoupdateperiod(self, autoupdateperiod):
        """Sets the autoupdateperiod of this AdminConfigUpdate.

        The interval (in minutes) for checking for new updates.  # noqa: E501

        :param autoupdateperiod: The autoupdateperiod of this AdminConfigUpdate.
        :type autoupdateperiod: int
        """

        self._autoupdateperiod = autoupdateperiod

    @property
    def deleteafterimport(self):
        """Gets the deleteafterimport of this AdminConfigUpdate.

        If you want to clean the pickup folder after the updates have been applied.  # noqa: E501

        :return: The deleteafterimport of this AdminConfigUpdate.
        :rtype: bool
        """
        return self._deleteafterimport

    @deleteafterimport.setter
    def deleteafterimport(self, deleteafterimport):
        """Sets the deleteafterimport of this AdminConfigUpdate.

        If you want to clean the pickup folder after the updates have been applied.  # noqa: E501

        :param deleteafterimport: The deleteafterimport of this AdminConfigUpdate.
        :type deleteafterimport: bool
        """

        self._deleteafterimport = deleteafterimport

    @property
    def disabledupdate(self):
        """Gets the disabledupdate of this AdminConfigUpdate.

        Lockdown a time interval when the engines are not allowed to update.  # noqa: E501

        :return: The disabledupdate of this AdminConfigUpdate.
        :rtype: List[AdminConfigUpdateDisabledupdate]
        """
        return self._disabledupdate

    @disabledupdate.setter
    def disabledupdate(self, disabledupdate):
        """Sets the disabledupdate of this AdminConfigUpdate.

        Lockdown a time interval when the engines are not allowed to update.  # noqa: E501

        :param disabledupdate: The disabledupdate of this AdminConfigUpdate.
        :type disabledupdate: List[AdminConfigUpdateDisabledupdate]
        """

        self._disabledupdate = disabledupdate

    @property
    def pickupfolder(self):
        """Gets the pickupfolder of this AdminConfigUpdate.

        The folder where MetaDefender will look for the new engine files.  # noqa: E501

        :return: The pickupfolder of this AdminConfigUpdate.
        :rtype: str
        """
        return self._pickupfolder

    @pickupfolder.setter
    def pickupfolder(self, pickupfolder):
        """Sets the pickupfolder of this AdminConfigUpdate.

        The folder where MetaDefender will look for the new engine files.  # noqa: E501

        :param pickupfolder: The pickupfolder of this AdminConfigUpdate.
        :type pickupfolder: str
        """

        self._pickupfolder = pickupfolder

    @property
    def source(self):
        """Gets the source of this AdminConfigUpdate.

        Define where the updates will be loaded from. <p> This can be either:   * `internet` -> if selected, will check for new updates every `autoupdateperiod` minutes   * `folder` -> make sure that MetaDefender has access/permission to that folder   * `manual` -> requires manually uploading the packages in Inventory > Modules > Upload package.   # noqa: E501

        :return: The source of this AdminConfigUpdate.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this AdminConfigUpdate.

        Define where the updates will be loaded from. <p> This can be either:   * `internet` -> if selected, will check for new updates every `autoupdateperiod` minutes   * `folder` -> make sure that MetaDefender has access/permission to that folder   * `manual` -> requires manually uploading the packages in Inventory > Modules > Upload package.   # noqa: E501

        :param source: The source of this AdminConfigUpdate.
        :type source: str
        """
        allowed_values = ["internet", "folder", "manual"]  # noqa: E501
        if source not in allowed_values:
            raise ValueError(
                "Invalid value for `source` ({0}), must be one of {1}"
                .format(source, allowed_values)
            )

        self._source = source
