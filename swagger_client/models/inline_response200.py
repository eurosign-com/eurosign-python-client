# coding: utf-8

"""
    Eurosign

    This is the documentation of the eurosign API, you can download all of our SDK in this page.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: apiteam@eurosign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class InlineResponse200(object):
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
        'uuid': 'str',
        'name': 'str',
        'sender_id': 'list[Object]',
        'creation_date': 'list[Object]',
        'send_date': 'list[Object]',
        'expiration_date': 'list[Object]',
        'status': 'list[Object]'
    }

    attribute_map = {
        'uuid': 'uuid',
        'name': 'name',
        'sender_id': 'senderId',
        'creation_date': 'creationDate',
        'send_date': 'sendDate',
        'expiration_date': 'expirationDate',
        'status': 'status'
    }

    def __init__(self, uuid=None, name=None, sender_id=None, creation_date=None, send_date=None, expiration_date=None, status=None):  # noqa: E501
        """InlineResponse200 - a model defined in Swagger"""  # noqa: E501
        self._uuid = None
        self._name = None
        self._sender_id = None
        self._creation_date = None
        self._send_date = None
        self._expiration_date = None
        self._status = None
        self.discriminator = None
        if uuid is not None:
            self.uuid = uuid
        if name is not None:
            self.name = name
        if sender_id is not None:
            self.sender_id = sender_id
        if creation_date is not None:
            self.creation_date = creation_date
        if send_date is not None:
            self.send_date = send_date
        if expiration_date is not None:
            self.expiration_date = expiration_date
        if status is not None:
            self.status = status

    @property
    def uuid(self):
        """Gets the uuid of this InlineResponse200.  # noqa: E501

        UUID of the signature request UUID  # noqa: E501

        :return: The uuid of this InlineResponse200.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this InlineResponse200.

        UUID of the signature request UUID  # noqa: E501

        :param uuid: The uuid of this InlineResponse200.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def name(self):
        """Gets the name of this InlineResponse200.  # noqa: E501

        Name of the signature request  # noqa: E501

        :return: The name of this InlineResponse200.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse200.

        Name of the signature request  # noqa: E501

        :param name: The name of this InlineResponse200.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def sender_id(self):
        """Gets the sender_id of this InlineResponse200.  # noqa: E501

        ID of the sender  # noqa: E501

        :return: The sender_id of this InlineResponse200.  # noqa: E501
        :rtype: list[Object]
        """
        return self._sender_id

    @sender_id.setter
    def sender_id(self, sender_id):
        """Sets the sender_id of this InlineResponse200.

        ID of the sender  # noqa: E501

        :param sender_id: The sender_id of this InlineResponse200.  # noqa: E501
        :type: list[Object]
        """

        self._sender_id = sender_id

    @property
    def creation_date(self):
        """Gets the creation_date of this InlineResponse200.  # noqa: E501

        Creation date of the signature request  # noqa: E501

        :return: The creation_date of this InlineResponse200.  # noqa: E501
        :rtype: list[Object]
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this InlineResponse200.

        Creation date of the signature request  # noqa: E501

        :param creation_date: The creation_date of this InlineResponse200.  # noqa: E501
        :type: list[Object]
        """

        self._creation_date = creation_date

    @property
    def send_date(self):
        """Gets the send_date of this InlineResponse200.  # noqa: E501

        Sending date of the signature request  # noqa: E501

        :return: The send_date of this InlineResponse200.  # noqa: E501
        :rtype: list[Object]
        """
        return self._send_date

    @send_date.setter
    def send_date(self, send_date):
        """Sets the send_date of this InlineResponse200.

        Sending date of the signature request  # noqa: E501

        :param send_date: The send_date of this InlineResponse200.  # noqa: E501
        :type: list[Object]
        """

        self._send_date = send_date

    @property
    def expiration_date(self):
        """Gets the expiration_date of this InlineResponse200.  # noqa: E501

        Expiration date of the signature request  # noqa: E501

        :return: The expiration_date of this InlineResponse200.  # noqa: E501
        :rtype: list[Object]
        """
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, expiration_date):
        """Sets the expiration_date of this InlineResponse200.

        Expiration date of the signature request  # noqa: E501

        :param expiration_date: The expiration_date of this InlineResponse200.  # noqa: E501
        :type: list[Object]
        """

        self._expiration_date = expiration_date

    @property
    def status(self):
        """Gets the status of this InlineResponse200.  # noqa: E501

        Status date of the signature request  # noqa: E501

        :return: The status of this InlineResponse200.  # noqa: E501
        :rtype: list[Object]
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InlineResponse200.

        Status date of the signature request  # noqa: E501

        :param status: The status of this InlineResponse200.  # noqa: E501
        :type: list[Object]
        """

        self._status = status

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
        if issubclass(InlineResponse200, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponse200):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
