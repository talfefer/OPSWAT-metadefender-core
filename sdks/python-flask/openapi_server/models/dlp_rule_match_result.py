# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class DLPRuleMatchResult(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, after=None, before=None, certainty=None, certainty_score=None, hit=None, is_redacted=None, severity=None):  # noqa: E501
        """DLPRuleMatchResult - a model defined in OpenAPI

        :param after: The after of this DLPRuleMatchResult.  # noqa: E501
        :type after: str
        :param before: The before of this DLPRuleMatchResult.  # noqa: E501
        :type before: str
        :param certainty: The certainty of this DLPRuleMatchResult.  # noqa: E501
        :type certainty: str
        :param certainty_score: The certainty_score of this DLPRuleMatchResult.  # noqa: E501
        :type certainty_score: int
        :param hit: The hit of this DLPRuleMatchResult.  # noqa: E501
        :type hit: str
        :param is_redacted: The is_redacted of this DLPRuleMatchResult.  # noqa: E501
        :type is_redacted: bool
        :param severity: The severity of this DLPRuleMatchResult.  # noqa: E501
        :type severity: int
        """
        self.openapi_types = {
            'after': str,
            'before': str,
            'certainty': str,
            'certainty_score': int,
            'hit': str,
            'is_redacted': bool,
            'severity': int
        }

        self.attribute_map = {
            'after': 'after',
            'before': 'before',
            'certainty': 'certainty',
            'certainty_score': 'certainty_score',
            'hit': 'hit',
            'is_redacted': 'isRedacted',
            'severity': 'severity'
        }

        self._after = after
        self._before = before
        self._certainty = certainty
        self._certainty_score = certainty_score
        self._hit = hit
        self._is_redacted = is_redacted
        self._severity = severity

    @classmethod
    def from_dict(cls, dikt) -> 'DLPRuleMatchResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DLPRuleMatchResult of this DLPRuleMatchResult.  # noqa: E501
        :rtype: DLPRuleMatchResult
        """
        return util.deserialize_model(dikt, cls)

    @property
    def after(self):
        """Gets the after of this DLPRuleMatchResult.

        The context after the matched data.  # noqa: E501

        :return: The after of this DLPRuleMatchResult.
        :rtype: str
        """
        return self._after

    @after.setter
    def after(self, after):
        """Sets the after of this DLPRuleMatchResult.

        The context after the matched data.  # noqa: E501

        :param after: The after of this DLPRuleMatchResult.
        :type after: str
        """

        self._after = after

    @property
    def before(self):
        """Gets the before of this DLPRuleMatchResult.

        The context before the matched data.  # noqa: E501

        :return: The before of this DLPRuleMatchResult.
        :rtype: str
        """
        return self._before

    @before.setter
    def before(self, before):
        """Sets the before of this DLPRuleMatchResult.

        The context before the matched data.  # noqa: E501

        :param before: The before of this DLPRuleMatchResult.
        :type before: str
        """

        self._before = before

    @property
    def certainty(self):
        """Gets the certainty of this DLPRuleMatchResult.

        The text version of \"certainty_score\", possible values:   * `Very Low`     * `Low`     * `Medium`     * `High`     * `Very High`   # noqa: E501

        :return: The certainty of this DLPRuleMatchResult.
        :rtype: str
        """
        return self._certainty

    @certainty.setter
    def certainty(self, certainty):
        """Sets the certainty of this DLPRuleMatchResult.

        The text version of \"certainty_score\", possible values:   * `Very Low`     * `Low`     * `Medium`     * `High`     * `Very High`   # noqa: E501

        :param certainty: The certainty of this DLPRuleMatchResult.
        :type certainty: str
        """
        allowed_values = ["Very Low", "Low", "Medium", "High", "Very High"]  # noqa: E501
        if certainty not in allowed_values:
            raise ValueError(
                "Invalid value for `certainty` ({0}), must be one of {1}"
                .format(certainty, allowed_values)
            )

        self._certainty = certainty

    @property
    def certainty_score(self):
        """Gets the certainty_score of this DLPRuleMatchResult.

        Is  defined by the relevance of the given hit in its context. It is calculated based on multiple factors such as the number of digits, possible values: [0-100]   # noqa: E501

        :return: The certainty_score of this DLPRuleMatchResult.
        :rtype: int
        """
        return self._certainty_score

    @certainty_score.setter
    def certainty_score(self, certainty_score):
        """Sets the certainty_score of this DLPRuleMatchResult.

        Is  defined by the relevance of the given hit in its context. It is calculated based on multiple factors such as the number of digits, possible values: [0-100]   # noqa: E501

        :param certainty_score: The certainty_score of this DLPRuleMatchResult.
        :type certainty_score: int
        """

        self._certainty_score = certainty_score

    @property
    def hit(self):
        """Gets the hit of this DLPRuleMatchResult.

        The matched data.  # noqa: E501

        :return: The hit of this DLPRuleMatchResult.
        :rtype: str
        """
        return self._hit

    @hit.setter
    def hit(self, hit):
        """Sets the hit of this DLPRuleMatchResult.

        The matched data.  # noqa: E501

        :param hit: The hit of this DLPRuleMatchResult.
        :type hit: str
        """

        self._hit = hit

    @property
    def is_redacted(self):
        """Gets the is_redacted of this DLPRuleMatchResult.

        If file was redacted or not.  # noqa: E501

        :return: The is_redacted of this DLPRuleMatchResult.
        :rtype: bool
        """
        return self._is_redacted

    @is_redacted.setter
    def is_redacted(self, is_redacted):
        """Sets the is_redacted of this DLPRuleMatchResult.

        If file was redacted or not.  # noqa: E501

        :param is_redacted: The is_redacted of this DLPRuleMatchResult.
        :type is_redacted: bool
        """

        self._is_redacted = is_redacted

    @property
    def severity(self):
        """Gets the severity of this DLPRuleMatchResult.

        (NOTE: this field is deprecated): can be 0 (detected) or 1 (suspicious).   # noqa: E501

        :return: The severity of this DLPRuleMatchResult.
        :rtype: int
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this DLPRuleMatchResult.

        (NOTE: this field is deprecated): can be 0 (detected) or 1 (suspicious).   # noqa: E501

        :param severity: The severity of this DLPRuleMatchResult.
        :type severity: int
        """
        allowed_values = [0, 1]  # noqa: E501
        if severity not in allowed_values:
            raise ValueError(
                "Invalid value for `severity` ({0}), must be one of {1}"
                .format(severity, allowed_values)
            )

        self._severity = severity
