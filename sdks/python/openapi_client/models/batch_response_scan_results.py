# coding: utf-8

"""
    MetaDefender Core

    ## Developer Guide This is the API documentation for *MetaDefender Core Public API*.  If you would like to evaluate or have any questions about this documentation, please contact us via our [Contact Us](https://opswat.com/contact) form.  ## How to Interact with MetaDefender Core using REST Beginning with MetaDefender Core 4.x, OPSWAT recommends using the JSON-based REST API. The available methods are documented below. > _**Note**:_ MetaDefender API doesn't support chunk upload, however is recommended to stream the files to MetaDefender as part of the upload process.  --- ## File Analysis Process    MetaDefender's main functionality is to analyze large volumes with a high throughput. Depending on the configuration and licensed technologies, the analysis times can vary.    Below is a brief description of the API integration flow:    1. Upload a file for analysis (`POST /file`), which returns the `data_id`: [File Analysis](#operation/fileAnalysisPost)).           > _**Note**:_ The performance depends on:           > - number of nodes (scaling)     > - number of engines per node     > - type of file to be scanned     > - Metadefender Core and nodes' hardware       2. You have 2 ways to retrieve the analysis report:      - **Polling**: Fetch the result with previously received data_id (`GET /file/{data_id}` resource) until scan result belonging to data_id doesn't reach the 100 percent progress_percentage: ( [Fetch processing result](#operation/userLogin))        > _**Note**:_ Too many data_id requests can reduce performance. It is enough to just check every few hundred milliseconds.          - **Callbackurl**: Specify a callbackurl that will be called once the analysis is complete.     3. Retrieve the analysis results anytime after the analysis is completed with hash for files (md5, sha1, sha256) by calling [Fetch processing result](#operation/userLogin).      - The hash can be found in the scan results    4. Retrieve processed file (sanitized, redacted, watermarked, etc.) after the analysis is complete.      > _**Note**:_ Based on the configured retention policy, the files might be available for retrieval at a later time.   --- OPSWAT provides some sample codes on [GitHub](https://github.com/OPSWAT) to make it easier to understand how the MetaDefender REST API works.   # noqa: E501

    The version of the OpenAPI document: v4.18.0
    Contact: feedback@opswat.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class BatchResponseScanResults(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'batch_id': 'str',
        'scan_all_result_a': 'ProcessingResultsStringEnum',
        'scan_all_result_i': 'ProcessingResultsIndexEnum',
        'start_time': 'str',
        'total_avs': 'int',
        'total_time': 'int'
    }

    attribute_map = {
        'batch_id': 'batch_id',
        'scan_all_result_a': 'scan_all_result_a',
        'scan_all_result_i': 'scan_all_result_i',
        'start_time': 'start_time',
        'total_avs': 'total_avs',
        'total_time': 'total_time'
    }

    def __init__(self, batch_id=None, scan_all_result_a=None, scan_all_result_i=None, start_time=None, total_avs=None, total_time=None, local_vars_configuration=None):  # noqa: E501
        """BatchResponseScanResults - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._batch_id = None
        self._scan_all_result_a = None
        self._scan_all_result_i = None
        self._start_time = None
        self._total_avs = None
        self._total_time = None
        self.discriminator = None

        if batch_id is not None:
            self.batch_id = batch_id
        if scan_all_result_a is not None:
            self.scan_all_result_a = scan_all_result_a
        if scan_all_result_i is not None:
            self.scan_all_result_i = scan_all_result_i
        if start_time is not None:
            self.start_time = start_time
        if total_avs is not None:
            self.total_avs = total_avs
        if total_time is not None:
            self.total_time = total_time

    @property
    def batch_id(self):
        """Gets the batch_id of this BatchResponseScanResults.  # noqa: E501

        The batch unique identifer  # noqa: E501

        :return: The batch_id of this BatchResponseScanResults.  # noqa: E501
        :rtype: str
        """
        return self._batch_id

    @batch_id.setter
    def batch_id(self, batch_id):
        """Sets the batch_id of this BatchResponseScanResults.

        The batch unique identifer  # noqa: E501

        :param batch_id: The batch_id of this BatchResponseScanResults.  # noqa: E501
        :type: str
        """

        self._batch_id = batch_id

    @property
    def scan_all_result_a(self):
        """Gets the scan_all_result_a of this BatchResponseScanResults.  # noqa: E501

        The overall scan result as string  # noqa: E501

        :return: The scan_all_result_a of this BatchResponseScanResults.  # noqa: E501
        :rtype: ProcessingResultsStringEnum
        """
        return self._scan_all_result_a

    @scan_all_result_a.setter
    def scan_all_result_a(self, scan_all_result_a):
        """Sets the scan_all_result_a of this BatchResponseScanResults.

        The overall scan result as string  # noqa: E501

        :param scan_all_result_a: The scan_all_result_a of this BatchResponseScanResults.  # noqa: E501
        :type: ProcessingResultsStringEnum
        """

        self._scan_all_result_a = scan_all_result_a

    @property
    def scan_all_result_i(self):
        """Gets the scan_all_result_i of this BatchResponseScanResults.  # noqa: E501

        The overall scan result as index in the Processing Results table.  # noqa: E501

        :return: The scan_all_result_i of this BatchResponseScanResults.  # noqa: E501
        :rtype: ProcessingResultsIndexEnum
        """
        return self._scan_all_result_i

    @scan_all_result_i.setter
    def scan_all_result_i(self, scan_all_result_i):
        """Sets the scan_all_result_i of this BatchResponseScanResults.

        The overall scan result as index in the Processing Results table.  # noqa: E501

        :param scan_all_result_i: The scan_all_result_i of this BatchResponseScanResults.  # noqa: E501
        :type: ProcessingResultsIndexEnum
        """

        self._scan_all_result_i = scan_all_result_i

    @property
    def start_time(self):
        """Gets the start_time of this BatchResponseScanResults.  # noqa: E501

        Timestamp when the scanning process starts.  # noqa: E501

        :return: The start_time of this BatchResponseScanResults.  # noqa: E501
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this BatchResponseScanResults.

        Timestamp when the scanning process starts.  # noqa: E501

        :param start_time: The start_time of this BatchResponseScanResults.  # noqa: E501
        :type: str
        """

        self._start_time = start_time

    @property
    def total_avs(self):
        """Gets the total_avs of this BatchResponseScanResults.  # noqa: E501

        Total number of scanning engines used as part of this analysis.  # noqa: E501

        :return: The total_avs of this BatchResponseScanResults.  # noqa: E501
        :rtype: int
        """
        return self._total_avs

    @total_avs.setter
    def total_avs(self, total_avs):
        """Sets the total_avs of this BatchResponseScanResults.

        Total number of scanning engines used as part of this analysis.  # noqa: E501

        :param total_avs: The total_avs of this BatchResponseScanResults.  # noqa: E501
        :type: int
        """

        self._total_avs = total_avs

    @property
    def total_time(self):
        """Gets the total_time of this BatchResponseScanResults.  # noqa: E501

        Total time elapsed during scan (in milliseconds).  # noqa: E501

        :return: The total_time of this BatchResponseScanResults.  # noqa: E501
        :rtype: int
        """
        return self._total_time

    @total_time.setter
    def total_time(self, total_time):
        """Sets the total_time of this BatchResponseScanResults.

        Total time elapsed during scan (in milliseconds).  # noqa: E501

        :param total_time: The total_time of this BatchResponseScanResults.  # noqa: E501
        :type: int
        """

        self._total_time = total_time

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BatchResponseScanResults):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BatchResponseScanResults):
            return True

        return self.to_dict() != other.to_dict()
