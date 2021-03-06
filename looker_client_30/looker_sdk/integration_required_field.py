# coding: utf-8

"""
    Looker API 3.0 Reference

    ### Authorization  The Looker API uses Looker **API3** credentials for authorization and access control. Looker admins can create API3 credentials on Looker's **Admin/Users** page. Pass API3 credentials to the **/login** endpoint to obtain a temporary access_token. Include that access_token in the Authorization header of Looker API requests. For details, see [Looker API Authorization](https://looker.com/docs/r/api/authorization)  ### Client SDKs  The Looker API is a RESTful system that should be usable by any programming language capable of making HTTPS requests. Client SDKs for a variety of programming languages can be generated from the Looker API's Swagger JSON metadata to streamline use of the Looker API in your applications. A client SDK for Ruby is available as an example. For more information, see [Looker API Client SDKs](https://looker.com/docs/r/api/client_sdks)  ### Try It Out!  The 'api-docs' page served by the Looker instance includes 'Try It Out!' buttons for each API method. After logging in with API3 credentials, you can use the \"Try It Out!\" buttons to call the API directly from the documentation page to interactively explore API features and responses.  ### Versioning  Future releases of Looker will expand this API release-by-release to securely expose more and more of the core power of Looker to API client applications. API endpoints marked as \"beta\" may receive breaking changes without warning. Stable (non-beta) API endpoints should not receive breaking changes in future releases. For more information, see [Looker API Versioning](https://looker.com/docs/r/api/versioning)   # noqa: E501

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class IntegrationRequiredField(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'tag': 'str',
        'any_tag': 'list[str]',
        'all_tags': 'list[str]'
    }

    attribute_map = {
        'tag': 'tag',
        'any_tag': 'any_tag',
        'all_tags': 'all_tags'
    }

    def __init__(self, tag=None, any_tag=None, all_tags=None):  # noqa: E501
        """IntegrationRequiredField - a model defined in Swagger"""  # noqa: E501

        self._tag = None
        self._any_tag = None
        self._all_tags = None
        self.discriminator = None

        if tag is not None:
            self.tag = tag
        if any_tag is not None:
            self.any_tag = any_tag
        if all_tags is not None:
            self.all_tags = all_tags

    @property
    def tag(self):
        """Gets the tag of this IntegrationRequiredField.  # noqa: E501

        Matches a field that has this tag.  # noqa: E501

        :return: The tag of this IntegrationRequiredField.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this IntegrationRequiredField.

        Matches a field that has this tag.  # noqa: E501

        :param tag: The tag of this IntegrationRequiredField.  # noqa: E501
        :type: str
        """

        self._tag = tag

    @property
    def any_tag(self):
        """Gets the any_tag of this IntegrationRequiredField.  # noqa: E501

        If present, supercedes 'tag' and matches a field that has any of the provided tags.  # noqa: E501

        :return: The any_tag of this IntegrationRequiredField.  # noqa: E501
        :rtype: list[str]
        """
        return self._any_tag

    @any_tag.setter
    def any_tag(self, any_tag):
        """Sets the any_tag of this IntegrationRequiredField.

        If present, supercedes 'tag' and matches a field that has any of the provided tags.  # noqa: E501

        :param any_tag: The any_tag of this IntegrationRequiredField.  # noqa: E501
        :type: list[str]
        """

        self._any_tag = any_tag

    @property
    def all_tags(self):
        """Gets the all_tags of this IntegrationRequiredField.  # noqa: E501

        If present, supercedes 'tag' and matches a field that has all of the provided tags.  # noqa: E501

        :return: The all_tags of this IntegrationRequiredField.  # noqa: E501
        :rtype: list[str]
        """
        return self._all_tags

    @all_tags.setter
    def all_tags(self, all_tags):
        """Sets the all_tags of this IntegrationRequiredField.

        If present, supercedes 'tag' and matches a field that has all of the provided tags.  # noqa: E501

        :param all_tags: The all_tags of this IntegrationRequiredField.  # noqa: E501
        :type: list[str]
        """

        self._all_tags = all_tags

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if not isinstance(other, IntegrationRequiredField):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
