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


class LicenseInformation(object):
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
        'days_left': 'int',
        'deployment': 'str',
        'expiration': 'str',
        'licensed_engines': 'list[str]',
        'max_node_count': 'str',
        'online_activated': 'bool',
        'product_id': 'str',
        'product_name': 'str'
    }

    attribute_map = {
        'days_left': 'days_left',
        'deployment': 'deployment',
        'expiration': 'expiration',
        'licensed_engines': 'licensed_engines',
        'max_node_count': 'max_node_count',
        'online_activated': 'online_activated',
        'product_id': 'product_id',
        'product_name': 'product_name'
    }

    def __init__(self, days_left=None, deployment=None, expiration=None, licensed_engines=None, max_node_count=None, online_activated=None, product_id=None, product_name=None, local_vars_configuration=None):  # noqa: E501
        """LicenseInformation - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._days_left = None
        self._deployment = None
        self._expiration = None
        self._licensed_engines = None
        self._max_node_count = None
        self._online_activated = None
        self._product_id = None
        self._product_name = None
        self.discriminator = None

        if days_left is not None:
            self.days_left = days_left
        if deployment is not None:
            self.deployment = deployment
        if expiration is not None:
            self.expiration = expiration
        if licensed_engines is not None:
            self.licensed_engines = licensed_engines
        if max_node_count is not None:
            self.max_node_count = max_node_count
        if online_activated is not None:
            self.online_activated = online_activated
        if product_id is not None:
            self.product_id = product_id
        if product_name is not None:
            self.product_name = product_name

    @property
    def days_left(self):
        """Gets the days_left of this LicenseInformation.  # noqa: E501

        Number of days left before expiration  # noqa: E501

        :return: The days_left of this LicenseInformation.  # noqa: E501
        :rtype: int
        """
        return self._days_left

    @days_left.setter
    def days_left(self, days_left):
        """Sets the days_left of this LicenseInformation.

        Number of days left before expiration  # noqa: E501

        :param days_left: The days_left of this LicenseInformation.  # noqa: E501
        :type: int
        """

        self._days_left = days_left

    @property
    def deployment(self):
        """Gets the deployment of this LicenseInformation.  # noqa: E501

        Unique identifier which is maps the current deployment to the activation  # noqa: E501

        :return: The deployment of this LicenseInformation.  # noqa: E501
        :rtype: str
        """
        return self._deployment

    @deployment.setter
    def deployment(self, deployment):
        """Sets the deployment of this LicenseInformation.

        Unique identifier which is maps the current deployment to the activation  # noqa: E501

        :param deployment: The deployment of this LicenseInformation.  # noqa: E501
        :type: str
        """

        self._deployment = deployment

    @property
    def expiration(self):
        """Gets the expiration of this LicenseInformation.  # noqa: E501

        Expiration date in MM/DD/YYYY format.  # noqa: E501

        :return: The expiration of this LicenseInformation.  # noqa: E501
        :rtype: str
        """
        return self._expiration

    @expiration.setter
    def expiration(self, expiration):
        """Sets the expiration of this LicenseInformation.

        Expiration date in MM/DD/YYYY format.  # noqa: E501

        :param expiration: The expiration of this LicenseInformation.  # noqa: E501
        :type: str
        """

        self._expiration = expiration

    @property
    def licensed_engines(self):
        """Gets the licensed_engines of this LicenseInformation.  # noqa: E501

        List of engine/module identifiers that have been licensed  # noqa: E501

        :return: The licensed_engines of this LicenseInformation.  # noqa: E501
        :rtype: list[str]
        """
        return self._licensed_engines

    @licensed_engines.setter
    def licensed_engines(self, licensed_engines):
        """Sets the licensed_engines of this LicenseInformation.

        List of engine/module identifiers that have been licensed  # noqa: E501

        :param licensed_engines: The licensed_engines of this LicenseInformation.  # noqa: E501
        :type: list[str]
        """

        self._licensed_engines = licensed_engines

    @property
    def max_node_count(self):
        """Gets the max_node_count of this LicenseInformation.  # noqa: E501

        Total number of deployed MetaDefender Nodes attached to this MetaDefender Core instance.  # noqa: E501

        :return: The max_node_count of this LicenseInformation.  # noqa: E501
        :rtype: str
        """
        return self._max_node_count

    @max_node_count.setter
    def max_node_count(self, max_node_count):
        """Sets the max_node_count of this LicenseInformation.

        Total number of deployed MetaDefender Nodes attached to this MetaDefender Core instance.  # noqa: E501

        :param max_node_count: The max_node_count of this LicenseInformation.  # noqa: E501
        :type: str
        """

        self._max_node_count = max_node_count

    @property
    def online_activated(self):
        """Gets the online_activated of this LicenseInformation.  # noqa: E501

        Track online/offline activation mode  # noqa: E501

        :return: The online_activated of this LicenseInformation.  # noqa: E501
        :rtype: bool
        """
        return self._online_activated

    @online_activated.setter
    def online_activated(self, online_activated):
        """Sets the online_activated of this LicenseInformation.

        Track online/offline activation mode  # noqa: E501

        :param online_activated: The online_activated of this LicenseInformation.  # noqa: E501
        :type: bool
        """

        self._online_activated = online_activated

    @property
    def product_id(self):
        """Gets the product_id of this LicenseInformation.  # noqa: E501

        Official MetaDefender base SKU licensed.  # noqa: E501

        :return: The product_id of this LicenseInformation.  # noqa: E501
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this LicenseInformation.

        Official MetaDefender base SKU licensed.  # noqa: E501

        :param product_id: The product_id of this LicenseInformation.  # noqa: E501
        :type: str
        """

        self._product_id = product_id

    @property
    def product_name(self):
        """Gets the product_name of this LicenseInformation.  # noqa: E501

        Official MetaDefender base product name licensed.  # noqa: E501

        :return: The product_name of this LicenseInformation.  # noqa: E501
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """Sets the product_name of this LicenseInformation.

        Official MetaDefender base product name licensed.  # noqa: E501

        :param product_name: The product_name of this LicenseInformation.  # noqa: E501
        :type: str
        """

        self._product_name = product_name

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
        if not isinstance(other, LicenseInformation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LicenseInformation):
            return True

        return self.to_dict() != other.to_dict()
