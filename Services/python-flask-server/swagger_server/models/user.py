# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class User(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, pseudo: str=None, password: str=None, expert_level: int=None, codepostal: int=None):  # noqa: E501
        """User - a model defined in Swagger

        :param pseudo: The pseudo of this User.  # noqa: E501
        :type pseudo: str
        :param password: The password of this User.  # noqa: E501
        :type password: str
        :param expert_level: The expert_level of this User.  # noqa: E501
        :type expert_level: int
        :param codepostal: The codepostal of this User.  # noqa: E501
        :type codepostal: int
        """
        self.swagger_types = {
            'pseudo': str,
            'password': str,
            'expert_level': int,
            'codepostal': int
        }

        self.attribute_map = {
            'pseudo': 'pseudo',
            'password': 'password',
            'expert_level': 'expert_level',
            'codepostal': 'codepostal'
        }

        self._pseudo = pseudo
        self._password = password
        self._expert_level = expert_level
        self._codepostal = codepostal

    @classmethod
    def from_dict(cls, dikt) -> 'User':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The User of this User.  # noqa: E501
        :rtype: User
        """
        return util.deserialize_model(dikt, cls)

    @property
    def pseudo(self) -> str:
        """Gets the pseudo of this User.


        :return: The pseudo of this User.
        :rtype: str
        """
        return self._pseudo

    @pseudo.setter
    def pseudo(self, pseudo: str):
        """Sets the pseudo of this User.


        :param pseudo: The pseudo of this User.
        :type pseudo: str
        """
        if pseudo is None:
            raise ValueError("Invalid value for `pseudo`, must not be `None`")  # noqa: E501

        self._pseudo = pseudo

    @property
    def password(self) -> str:
        """Gets the password of this User.


        :return: The password of this User.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password: str):
        """Sets the password of this User.


        :param password: The password of this User.
        :type password: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

    @property
    def expert_level(self) -> int:
        """Gets the expert_level of this User.


        :return: The expert_level of this User.
        :rtype: int
        """
        return self._expert_level

    @expert_level.setter
    def expert_level(self, expert_level: int):
        """Sets the expert_level of this User.


        :param expert_level: The expert_level of this User.
        :type expert_level: int
        """

        self._expert_level = expert_level

    @property
    def codepostal(self) -> int:
        """Gets the codepostal of this User.


        :return: The codepostal of this User.
        :rtype: int
        """
        return self._codepostal

    @codepostal.setter
    def codepostal(self, codepostal: int):
        """Sets the codepostal of this User.


        :param codepostal: The codepostal of this User.
        :type codepostal: int
        """
        if codepostal is None:
            raise ValueError("Invalid value for `codepostal`, must not be `None`")  # noqa: E501

        self._codepostal = codepostal
