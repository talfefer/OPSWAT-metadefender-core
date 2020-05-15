# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class FileInformation(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, display_name=None, file_size=None, file_type=None, file_type_description=None, md5=None, sha1=None, sha256=None, upload_timestamp=None):  # noqa: E501
        """FileInformation - a model defined in OpenAPI

        :param display_name: The display_name of this FileInformation.  # noqa: E501
        :type display_name: str
        :param file_size: The file_size of this FileInformation.  # noqa: E501
        :type file_size: int
        :param file_type: The file_type of this FileInformation.  # noqa: E501
        :type file_type: str
        :param file_type_description: The file_type_description of this FileInformation.  # noqa: E501
        :type file_type_description: str
        :param md5: The md5 of this FileInformation.  # noqa: E501
        :type md5: str
        :param sha1: The sha1 of this FileInformation.  # noqa: E501
        :type sha1: str
        :param sha256: The sha256 of this FileInformation.  # noqa: E501
        :type sha256: str
        :param upload_timestamp: The upload_timestamp of this FileInformation.  # noqa: E501
        :type upload_timestamp: str
        """
        self.openapi_types = {
            'display_name': str,
            'file_size': int,
            'file_type': str,
            'file_type_description': str,
            'md5': str,
            'sha1': str,
            'sha256': str,
            'upload_timestamp': str
        }

        self.attribute_map = {
            'display_name': 'display_name',
            'file_size': 'file_size',
            'file_type': 'file_type',
            'file_type_description': 'file_type_description',
            'md5': 'md5',
            'sha1': 'sha1',
            'sha256': 'sha256',
            'upload_timestamp': 'upload_timestamp'
        }

        self._display_name = display_name
        self._file_size = file_size
        self._file_type = file_type
        self._file_type_description = file_type_description
        self._md5 = md5
        self._sha1 = sha1
        self._sha256 = sha256
        self._upload_timestamp = upload_timestamp

    @classmethod
    def from_dict(cls, dikt) -> 'FileInformation':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The FileInformation of this FileInformation.  # noqa: E501
        :rtype: FileInformation
        """
        return util.deserialize_model(dikt, cls)

    @property
    def display_name(self):
        """Gets the display_name of this FileInformation.

        The filename reported via `filename` header.  # noqa: E501

        :return: The display_name of this FileInformation.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this FileInformation.

        The filename reported via `filename` header.  # noqa: E501

        :param display_name: The display_name of this FileInformation.
        :type display_name: str
        """

        self._display_name = display_name

    @property
    def file_size(self):
        """Gets the file_size of this FileInformation.

        Total file size in bytes.  # noqa: E501

        :return: The file_size of this FileInformation.
        :rtype: int
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        """Sets the file_size of this FileInformation.

        Total file size in bytes.  # noqa: E501

        :param file_size: The file_size of this FileInformation.
        :type file_size: int
        """

        self._file_size = file_size

    @property
    def file_type(self):
        """Gets the file_type of this FileInformation.

        The filetype using mimetype.  # noqa: E501

        :return: The file_type of this FileInformation.
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        """Sets the file_type of this FileInformation.

        The filetype using mimetype.  # noqa: E501

        :param file_type: The file_type of this FileInformation.
        :type file_type: str
        """

        self._file_type = file_type

    @property
    def file_type_description(self):
        """Gets the file_type_description of this FileInformation.

        The filetype in human readable format.  # noqa: E501

        :return: The file_type_description of this FileInformation.
        :rtype: str
        """
        return self._file_type_description

    @file_type_description.setter
    def file_type_description(self, file_type_description):
        """Sets the file_type_description of this FileInformation.

        The filetype in human readable format.  # noqa: E501

        :param file_type_description: The file_type_description of this FileInformation.
        :type file_type_description: str
        """

        self._file_type_description = file_type_description

    @property
    def md5(self):
        """Gets the md5 of this FileInformation.

        File's MD5 hash.  # noqa: E501

        :return: The md5 of this FileInformation.
        :rtype: str
        """
        return self._md5

    @md5.setter
    def md5(self, md5):
        """Sets the md5 of this FileInformation.

        File's MD5 hash.  # noqa: E501

        :param md5: The md5 of this FileInformation.
        :type md5: str
        """

        self._md5 = md5

    @property
    def sha1(self):
        """Gets the sha1 of this FileInformation.

        File's SHA1 hash.  # noqa: E501

        :return: The sha1 of this FileInformation.
        :rtype: str
        """
        return self._sha1

    @sha1.setter
    def sha1(self, sha1):
        """Sets the sha1 of this FileInformation.

        File's SHA1 hash.  # noqa: E501

        :param sha1: The sha1 of this FileInformation.
        :type sha1: str
        """

        self._sha1 = sha1

    @property
    def sha256(self):
        """Gets the sha256 of this FileInformation.

        File's SHA256 Hash.  # noqa: E501

        :return: The sha256 of this FileInformation.
        :rtype: str
        """
        return self._sha256

    @sha256.setter
    def sha256(self, sha256):
        """Sets the sha256 of this FileInformation.

        File's SHA256 Hash.  # noqa: E501

        :param sha256: The sha256 of this FileInformation.
        :type sha256: str
        """

        self._sha256 = sha256

    @property
    def upload_timestamp(self):
        """Gets the upload_timestamp of this FileInformation.

        The timestamp when file was successfully uploaded to MetaDefender.  # noqa: E501

        :return: The upload_timestamp of this FileInformation.
        :rtype: str
        """
        return self._upload_timestamp

    @upload_timestamp.setter
    def upload_timestamp(self, upload_timestamp):
        """Sets the upload_timestamp of this FileInformation.

        The timestamp when file was successfully uploaded to MetaDefender.  # noqa: E501

        :param upload_timestamp: The upload_timestamp of this FileInformation.
        :type upload_timestamp: str
        """

        self._upload_timestamp = upload_timestamp
