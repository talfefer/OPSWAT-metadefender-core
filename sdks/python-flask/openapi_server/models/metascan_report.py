# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.metascan_report_scan_details import MetascanReportScanDetails
from openapi_server.models.processing_results_index_enum import ProcessingResultsIndexEnum
from openapi_server.models.processing_results_string_enum import ProcessingResultsStringEnum
from openapi_server import util

from openapi_server.models.metascan_report_scan_details import MetascanReportScanDetails  # noqa: E501
from openapi_server.models.processing_results_index_enum import ProcessingResultsIndexEnum  # noqa: E501
from openapi_server.models.processing_results_string_enum import ProcessingResultsStringEnum  # noqa: E501

class MetascanReport(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, data_id=None, progress_percentage=None, scan_all_result_a=None, scan_all_result_i=None, start_time=None, total_avs=None, total_time=None, scan_details=None):  # noqa: E501
        """MetascanReport - a model defined in OpenAPI

        :param data_id: The data_id of this MetascanReport.  # noqa: E501
        :type data_id: str
        :param progress_percentage: The progress_percentage of this MetascanReport.  # noqa: E501
        :type progress_percentage: int
        :param scan_all_result_a: The scan_all_result_a of this MetascanReport.  # noqa: E501
        :type scan_all_result_a: ProcessingResultsStringEnum
        :param scan_all_result_i: The scan_all_result_i of this MetascanReport.  # noqa: E501
        :type scan_all_result_i: ProcessingResultsIndexEnum
        :param start_time: The start_time of this MetascanReport.  # noqa: E501
        :type start_time: str
        :param total_avs: The total_avs of this MetascanReport.  # noqa: E501
        :type total_avs: int
        :param total_time: The total_time of this MetascanReport.  # noqa: E501
        :type total_time: int
        :param scan_details: The scan_details of this MetascanReport.  # noqa: E501
        :type scan_details: MetascanReportScanDetails
        """
        self.openapi_types = {
            'data_id': str,
            'progress_percentage': int,
            'scan_all_result_a': ProcessingResultsStringEnum,
            'scan_all_result_i': ProcessingResultsIndexEnum,
            'start_time': str,
            'total_avs': int,
            'total_time': int,
            'scan_details': MetascanReportScanDetails
        }

        self.attribute_map = {
            'data_id': 'data_id',
            'progress_percentage': 'progress_percentage',
            'scan_all_result_a': 'scan_all_result_a',
            'scan_all_result_i': 'scan_all_result_i',
            'start_time': 'start_time',
            'total_avs': 'total_avs',
            'total_time': 'total_time',
            'scan_details': 'scan_details'
        }

        self._data_id = data_id
        self._progress_percentage = progress_percentage
        self._scan_all_result_a = scan_all_result_a
        self._scan_all_result_i = scan_all_result_i
        self._start_time = start_time
        self._total_avs = total_avs
        self._total_time = total_time
        self._scan_details = scan_details

    @classmethod
    def from_dict(cls, dikt) -> 'MetascanReport':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MetascanReport of this MetascanReport.  # noqa: E501
        :rtype: MetascanReport
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data_id(self):
        """Gets the data_id of this MetascanReport.

        Data ID of the requested file  # noqa: E501

        :return: The data_id of this MetascanReport.
        :rtype: str
        """
        return self._data_id

    @data_id.setter
    def data_id(self, data_id):
        """Sets the data_id of this MetascanReport.

        Data ID of the requested file  # noqa: E501

        :param data_id: The data_id of this MetascanReport.
        :type data_id: str
        """

        self._data_id = data_id

    @property
    def progress_percentage(self):
        """Gets the progress_percentage of this MetascanReport.

        Track analysis progress until reaches 100.  # noqa: E501

        :return: The progress_percentage of this MetascanReport.
        :rtype: int
        """
        return self._progress_percentage

    @progress_percentage.setter
    def progress_percentage(self, progress_percentage):
        """Sets the progress_percentage of this MetascanReport.

        Track analysis progress until reaches 100.  # noqa: E501

        :param progress_percentage: The progress_percentage of this MetascanReport.
        :type progress_percentage: int
        """

        self._progress_percentage = progress_percentage

    @property
    def scan_all_result_a(self):
        """Gets the scan_all_result_a of this MetascanReport.

        The overall scan result as string  # noqa: E501

        :return: The scan_all_result_a of this MetascanReport.
        :rtype: ProcessingResultsStringEnum
        """
        return self._scan_all_result_a

    @scan_all_result_a.setter
    def scan_all_result_a(self, scan_all_result_a):
        """Sets the scan_all_result_a of this MetascanReport.

        The overall scan result as string  # noqa: E501

        :param scan_all_result_a: The scan_all_result_a of this MetascanReport.
        :type scan_all_result_a: ProcessingResultsStringEnum
        """

        self._scan_all_result_a = scan_all_result_a

    @property
    def scan_all_result_i(self):
        """Gets the scan_all_result_i of this MetascanReport.

        The overall scan result as index in the Processing Results table.  # noqa: E501

        :return: The scan_all_result_i of this MetascanReport.
        :rtype: ProcessingResultsIndexEnum
        """
        return self._scan_all_result_i

    @scan_all_result_i.setter
    def scan_all_result_i(self, scan_all_result_i):
        """Sets the scan_all_result_i of this MetascanReport.

        The overall scan result as index in the Processing Results table.  # noqa: E501

        :param scan_all_result_i: The scan_all_result_i of this MetascanReport.
        :type scan_all_result_i: ProcessingResultsIndexEnum
        """

        self._scan_all_result_i = scan_all_result_i

    @property
    def start_time(self):
        """Gets the start_time of this MetascanReport.

        Timestamp when the scanning process starts.  # noqa: E501

        :return: The start_time of this MetascanReport.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this MetascanReport.

        Timestamp when the scanning process starts.  # noqa: E501

        :param start_time: The start_time of this MetascanReport.
        :type start_time: str
        """

        self._start_time = start_time

    @property
    def total_avs(self):
        """Gets the total_avs of this MetascanReport.

        Total number of scanning engines used as part of this analysis.  # noqa: E501

        :return: The total_avs of this MetascanReport.
        :rtype: int
        """
        return self._total_avs

    @total_avs.setter
    def total_avs(self, total_avs):
        """Sets the total_avs of this MetascanReport.

        Total number of scanning engines used as part of this analysis.  # noqa: E501

        :param total_avs: The total_avs of this MetascanReport.
        :type total_avs: int
        """

        self._total_avs = total_avs

    @property
    def total_time(self):
        """Gets the total_time of this MetascanReport.

        Total time elapsed during scan (in milliseconds).  # noqa: E501

        :return: The total_time of this MetascanReport.
        :rtype: int
        """
        return self._total_time

    @total_time.setter
    def total_time(self, total_time):
        """Sets the total_time of this MetascanReport.

        Total time elapsed during scan (in milliseconds).  # noqa: E501

        :param total_time: The total_time of this MetascanReport.
        :type total_time: int
        """

        self._total_time = total_time

    @property
    def scan_details(self):
        """Gets the scan_details of this MetascanReport.


        :return: The scan_details of this MetascanReport.
        :rtype: MetascanReportScanDetails
        """
        return self._scan_details

    @scan_details.setter
    def scan_details(self, scan_details):
        """Sets the scan_details of this MetascanReport.


        :param scan_details: The scan_details of this MetascanReport.
        :type scan_details: MetascanReportScanDetails
        """

        self._scan_details = scan_details
