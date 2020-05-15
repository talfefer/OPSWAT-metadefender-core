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


class AnalysisResultProcessInfo(object):
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
        'blocked_reason': 'str',
        'file_type_skipped_scan': 'bool',
        'outdated_data': 'list[str]',
        'processing_time': 'int',
        'profile': 'str',
        'progress_percentage': 'int',
        'queue_time': 'int',
        'result': 'str',
        'user_agent': 'str',
        'username': 'str',
        'verdicts': 'list[str]',
        'post_processing': 'AnalysisResultProcessInfoPostProcessing'
    }

    attribute_map = {
        'blocked_reason': 'blocked_reason',
        'file_type_skipped_scan': 'file_type_skipped_scan',
        'outdated_data': 'outdated_data',
        'processing_time': 'processing_time',
        'profile': 'profile',
        'progress_percentage': 'progress_percentage',
        'queue_time': 'queue_time',
        'result': 'result',
        'user_agent': 'user_agent',
        'username': 'username',
        'verdicts': 'verdicts',
        'post_processing': 'post_processing'
    }

    def __init__(self, blocked_reason=None, file_type_skipped_scan=None, outdated_data=None, processing_time=None, profile=None, progress_percentage=None, queue_time=None, result=None, user_agent=None, username=None, verdicts=None, post_processing=None, local_vars_configuration=None):  # noqa: E501
        """AnalysisResultProcessInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._blocked_reason = None
        self._file_type_skipped_scan = None
        self._outdated_data = None
        self._processing_time = None
        self._profile = None
        self._progress_percentage = None
        self._queue_time = None
        self._result = None
        self._user_agent = None
        self._username = None
        self._verdicts = None
        self._post_processing = None
        self.discriminator = None

        if blocked_reason is not None:
            self.blocked_reason = blocked_reason
        if file_type_skipped_scan is not None:
            self.file_type_skipped_scan = file_type_skipped_scan
        if outdated_data is not None:
            self.outdated_data = outdated_data
        if processing_time is not None:
            self.processing_time = processing_time
        if profile is not None:
            self.profile = profile
        if progress_percentage is not None:
            self.progress_percentage = progress_percentage
        if queue_time is not None:
            self.queue_time = queue_time
        if result is not None:
            self.result = result
        if user_agent is not None:
            self.user_agent = user_agent
        if username is not None:
            self.username = username
        if verdicts is not None:
            self.verdicts = verdicts
        if post_processing is not None:
            self.post_processing = post_processing

    @property
    def blocked_reason(self):
        """Gets the blocked_reason of this AnalysisResultProcessInfo.  # noqa: E501

        Provides the reason why the file is blocked (if so).  # noqa: E501

        :return: The blocked_reason of this AnalysisResultProcessInfo.  # noqa: E501
        :rtype: str
        """
        return self._blocked_reason

    @blocked_reason.setter
    def blocked_reason(self, blocked_reason):
        """Sets the blocked_reason of this AnalysisResultProcessInfo.

        Provides the reason why the file is blocked (if so).  # noqa: E501

        :param blocked_reason: The blocked_reason of this AnalysisResultProcessInfo.  # noqa: E501
        :type: str
        """

        self._blocked_reason = blocked_reason

    @property
    def file_type_skipped_scan(self):
        """Gets the file_type_skipped_scan of this AnalysisResultProcessInfo.  # noqa: E501

        Indicates if the input file's detected type was configured to skip scanning.  # noqa: E501

        :return: The file_type_skipped_scan of this AnalysisResultProcessInfo.  # noqa: E501
        :rtype: bool
        """
        return self._file_type_skipped_scan

    @file_type_skipped_scan.setter
    def file_type_skipped_scan(self, file_type_skipped_scan):
        """Sets the file_type_skipped_scan of this AnalysisResultProcessInfo.

        Indicates if the input file's detected type was configured to skip scanning.  # noqa: E501

        :param file_type_skipped_scan: The file_type_skipped_scan of this AnalysisResultProcessInfo.  # noqa: E501
        :type: bool
        """

        self._file_type_skipped_scan = file_type_skipped_scan

    @property
    def outdated_data(self):
        """Gets the outdated_data of this AnalysisResultProcessInfo.  # noqa: E501

        array of flags - if occur - describing outdated data in the result, these can be   * enginedefinitions: at least one of the AV engines the item was scanned with has a newer definition database   * configuration: the process' rule - or any item used by the rule - was modified since the item was processed   * sanitization: if item was sanitized this flag notifies that the sanitization information regarding this result is outdated, meaning the sanitized item is no longer available                 # noqa: E501

        :return: The outdated_data of this AnalysisResultProcessInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._outdated_data

    @outdated_data.setter
    def outdated_data(self, outdated_data):
        """Sets the outdated_data of this AnalysisResultProcessInfo.

        array of flags - if occur - describing outdated data in the result, these can be   * enginedefinitions: at least one of the AV engines the item was scanned with has a newer definition database   * configuration: the process' rule - or any item used by the rule - was modified since the item was processed   * sanitization: if item was sanitized this flag notifies that the sanitization information regarding this result is outdated, meaning the sanitized item is no longer available                 # noqa: E501

        :param outdated_data: The outdated_data of this AnalysisResultProcessInfo.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["enginedefinition", "configuration", "sanitization"]  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                not set(outdated_data).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `outdated_data` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(outdated_data) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._outdated_data = outdated_data

    @property
    def processing_time(self):
        """Gets the processing_time of this AnalysisResultProcessInfo.  # noqa: E501

        Total time elapsed during processing file on the node (in milliseconds).  # noqa: E501

        :return: The processing_time of this AnalysisResultProcessInfo.  # noqa: E501
        :rtype: int
        """
        return self._processing_time

    @processing_time.setter
    def processing_time(self, processing_time):
        """Sets the processing_time of this AnalysisResultProcessInfo.

        Total time elapsed during processing file on the node (in milliseconds).  # noqa: E501

        :param processing_time: The processing_time of this AnalysisResultProcessInfo.  # noqa: E501
        :type: int
        """

        self._processing_time = processing_time

    @property
    def profile(self):
        """Gets the profile of this AnalysisResultProcessInfo.  # noqa: E501

        The used rule name.  # noqa: E501

        :return: The profile of this AnalysisResultProcessInfo.  # noqa: E501
        :rtype: str
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        """Sets the profile of this AnalysisResultProcessInfo.

        The used rule name.  # noqa: E501

        :param profile: The profile of this AnalysisResultProcessInfo.  # noqa: E501
        :type: str
        """

        self._profile = profile

    @property
    def progress_percentage(self):
        """Gets the progress_percentage of this AnalysisResultProcessInfo.  # noqa: E501

        Percentage of processing completed (from 1-100).  # noqa: E501

        :return: The progress_percentage of this AnalysisResultProcessInfo.  # noqa: E501
        :rtype: int
        """
        return self._progress_percentage

    @progress_percentage.setter
    def progress_percentage(self, progress_percentage):
        """Sets the progress_percentage of this AnalysisResultProcessInfo.

        Percentage of processing completed (from 1-100).  # noqa: E501

        :param progress_percentage: The progress_percentage of this AnalysisResultProcessInfo.  # noqa: E501
        :type: int
        """

        self._progress_percentage = progress_percentage

    @property
    def queue_time(self):
        """Gets the queue_time of this AnalysisResultProcessInfo.  # noqa: E501

        Total time elapsed while the file waits in the queue (in milliseconds).  # noqa: E501

        :return: The queue_time of this AnalysisResultProcessInfo.  # noqa: E501
        :rtype: int
        """
        return self._queue_time

    @queue_time.setter
    def queue_time(self, queue_time):
        """Sets the queue_time of this AnalysisResultProcessInfo.

        Total time elapsed while the file waits in the queue (in milliseconds).  # noqa: E501

        :param queue_time: The queue_time of this AnalysisResultProcessInfo.  # noqa: E501
        :type: int
        """

        self._queue_time = queue_time

    @property
    def result(self):
        """Gets the result of this AnalysisResultProcessInfo.  # noqa: E501

        The final result of processing the file (Allowed / Blocked / Processing).  # noqa: E501

        :return: The result of this AnalysisResultProcessInfo.  # noqa: E501
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this AnalysisResultProcessInfo.

        The final result of processing the file (Allowed / Blocked / Processing).  # noqa: E501

        :param result: The result of this AnalysisResultProcessInfo.  # noqa: E501
        :type: str
        """

        self._result = result

    @property
    def user_agent(self):
        """Gets the user_agent of this AnalysisResultProcessInfo.  # noqa: E501

        Identifier for the REST Client that calls the API.  # noqa: E501

        :return: The user_agent of this AnalysisResultProcessInfo.  # noqa: E501
        :rtype: str
        """
        return self._user_agent

    @user_agent.setter
    def user_agent(self, user_agent):
        """Sets the user_agent of this AnalysisResultProcessInfo.

        Identifier for the REST Client that calls the API.  # noqa: E501

        :param user_agent: The user_agent of this AnalysisResultProcessInfo.  # noqa: E501
        :type: str
        """

        self._user_agent = user_agent

    @property
    def username(self):
        """Gets the username of this AnalysisResultProcessInfo.  # noqa: E501

        User identifier who submitted scan request earlier.  # noqa: E501

        :return: The username of this AnalysisResultProcessInfo.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this AnalysisResultProcessInfo.

        User identifier who submitted scan request earlier.  # noqa: E501

        :param username: The username of this AnalysisResultProcessInfo.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def verdicts(self):
        """Gets the verdicts of this AnalysisResultProcessInfo.  # noqa: E501

        Aggregated list of potential issues.  # noqa: E501

        :return: The verdicts of this AnalysisResultProcessInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._verdicts

    @verdicts.setter
    def verdicts(self, verdicts):
        """Sets the verdicts of this AnalysisResultProcessInfo.

        Aggregated list of potential issues.  # noqa: E501

        :param verdicts: The verdicts of this AnalysisResultProcessInfo.  # noqa: E501
        :type: list[str]
        """

        self._verdicts = verdicts

    @property
    def post_processing(self):
        """Gets the post_processing of this AnalysisResultProcessInfo.  # noqa: E501


        :return: The post_processing of this AnalysisResultProcessInfo.  # noqa: E501
        :rtype: AnalysisResultProcessInfoPostProcessing
        """
        return self._post_processing

    @post_processing.setter
    def post_processing(self, post_processing):
        """Sets the post_processing of this AnalysisResultProcessInfo.


        :param post_processing: The post_processing of this AnalysisResultProcessInfo.  # noqa: E501
        :type: AnalysisResultProcessInfoPostProcessing
        """

        self._post_processing = post_processing

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
        if not isinstance(other, AnalysisResultProcessInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AnalysisResultProcessInfo):
            return True

        return self.to_dict() != other.to_dict()
