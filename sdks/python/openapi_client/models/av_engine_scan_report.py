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


class AVEngineScanReport(object):
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
        'def_time': 'str',
        'eng_id': 'str',
        'location': 'str',
        'scan_result_i': 'int',
        'scan_time': 'int',
        'threat_found': 'str',
        'wait_time': 'int'
    }

    attribute_map = {
        'def_time': 'def_time',
        'eng_id': 'eng_id',
        'location': 'location',
        'scan_result_i': 'scan_result_i',
        'scan_time': 'scan_time',
        'threat_found': 'threat_found',
        'wait_time': 'wait_time'
    }

    def __init__(self, def_time=None, eng_id=None, location=None, scan_result_i=None, scan_time=None, threat_found=None, wait_time=None, local_vars_configuration=None):  # noqa: E501
        """AVEngineScanReport - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._def_time = None
        self._eng_id = None
        self._location = None
        self._scan_result_i = None
        self._scan_time = None
        self._threat_found = None
        self._wait_time = None
        self.discriminator = None

        if def_time is not None:
            self.def_time = def_time
        if eng_id is not None:
            self.eng_id = eng_id
        if location is not None:
            self.location = location
        if scan_result_i is not None:
            self.scan_result_i = scan_result_i
        if scan_time is not None:
            self.scan_time = scan_time
        if threat_found is not None:
            self.threat_found = threat_found
        if wait_time is not None:
            self.wait_time = wait_time

    @property
    def def_time(self):
        """Gets the def_time of this AVEngineScanReport.  # noqa: E501

        The database definition time for this engine  # noqa: E501

        :return: The def_time of this AVEngineScanReport.  # noqa: E501
        :rtype: str
        """
        return self._def_time

    @def_time.setter
    def def_time(self, def_time):
        """Sets the def_time of this AVEngineScanReport.

        The database definition time for this engine  # noqa: E501

        :param def_time: The def_time of this AVEngineScanReport.  # noqa: E501
        :type: str
        """

        self._def_time = def_time

    @property
    def eng_id(self):
        """Gets the eng_id of this AVEngineScanReport.  # noqa: E501

        The  unique identification string for the engine  # noqa: E501

        :return: The eng_id of this AVEngineScanReport.  # noqa: E501
        :rtype: str
        """
        return self._eng_id

    @eng_id.setter
    def eng_id(self, eng_id):
        """Sets the eng_id of this AVEngineScanReport.

        The  unique identification string for the engine  # noqa: E501

        :param eng_id: The eng_id of this AVEngineScanReport.  # noqa: E501
        :type: str
        """

        self._eng_id = eng_id

    @property
    def location(self):
        """Gets the location of this AVEngineScanReport.  # noqa: E501

        Where this engine is deployed (local/remote).  # noqa: E501

        :return: The location of this AVEngineScanReport.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this AVEngineScanReport.

        Where this engine is deployed (local/remote).  # noqa: E501

        :param location: The location of this AVEngineScanReport.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def scan_result_i(self):
        """Gets the scan_result_i of this AVEngineScanReport.  # noqa: E501

        Scan result as index in the Processing Results table  # noqa: E501

        :return: The scan_result_i of this AVEngineScanReport.  # noqa: E501
        :rtype: int
        """
        return self._scan_result_i

    @scan_result_i.setter
    def scan_result_i(self, scan_result_i):
        """Sets the scan_result_i of this AVEngineScanReport.

        Scan result as index in the Processing Results table  # noqa: E501

        :param scan_result_i: The scan_result_i of this AVEngineScanReport.  # noqa: E501
        :type: int
        """

        self._scan_result_i = scan_result_i

    @property
    def scan_time(self):
        """Gets the scan_time of this AVEngineScanReport.  # noqa: E501

        The time elapsed during scan with this engine (in milliseconds).  # noqa: E501

        :return: The scan_time of this AVEngineScanReport.  # noqa: E501
        :rtype: int
        """
        return self._scan_time

    @scan_time.setter
    def scan_time(self, scan_time):
        """Sets the scan_time of this AVEngineScanReport.

        The time elapsed during scan with this engine (in milliseconds).  # noqa: E501

        :param scan_time: The scan_time of this AVEngineScanReport.  # noqa: E501
        :type: int
        """

        self._scan_time = scan_time

    @property
    def threat_found(self):
        """Gets the threat_found of this AVEngineScanReport.  # noqa: E501

        The threat name, IF scan result is Infected or Suspicious. Otherwise empty string or error message from the engine.  # noqa: E501

        :return: The threat_found of this AVEngineScanReport.  # noqa: E501
        :rtype: str
        """
        return self._threat_found

    @threat_found.setter
    def threat_found(self, threat_found):
        """Sets the threat_found of this AVEngineScanReport.

        The threat name, IF scan result is Infected or Suspicious. Otherwise empty string or error message from the engine.  # noqa: E501

        :param threat_found: The threat_found of this AVEngineScanReport.  # noqa: E501
        :type: str
        """

        self._threat_found = threat_found

    @property
    def wait_time(self):
        """Gets the wait_time of this AVEngineScanReport.  # noqa: E501

        Time elapsed between sending file to node and receiving the result from the engine (in milliseconds).  # noqa: E501

        :return: The wait_time of this AVEngineScanReport.  # noqa: E501
        :rtype: int
        """
        return self._wait_time

    @wait_time.setter
    def wait_time(self, wait_time):
        """Sets the wait_time of this AVEngineScanReport.

        Time elapsed between sending file to node and receiving the result from the engine (in milliseconds).  # noqa: E501

        :param wait_time: The wait_time of this AVEngineScanReport.  # noqa: E501
        :type: int
        """

        self._wait_time = wait_time

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
        if not isinstance(other, AVEngineScanReport):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AVEngineScanReport):
            return True

        return self.to_dict() != other.to_dict()
