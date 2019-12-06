# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Changer(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, pseudo: str=None, password: str=None, new_password: str=None, expert_level: int=None, codepostal: int=None):  # noqa: E501
        """Changer - a model defined in Swagger

        :param pseudo: The pseudo of this Changer.  # noqa: E501
        :type pseudo: str
        :param password: The password of this Changer.  # noqa: E501
        :type password: str
        :param new_password: The new_password of this Changer.  # noqa: E501
        :type new_password: str
        :param expert_level: The expert_level of this Changer.  # noqa: E501
        :type expert_level: int
        :param codepostal: The codepostal of this Changer.  # noqa: E501
        :type codepostal: int
        """
        self.swagger_types = {
            'pseudo': str,
            'password': str,
            'new_password': str,
            'expert_level': int,
            'codepostal': int
        }

        self.attribute_map = {
            'pseudo': 'pseudo',
            'password': 'password',
            'new_password': 'new password',
            'expert_level': 'expert_level',
            'codepostal': 'codepostal'
        }

        self._pseudo = pseudo
        self._password = password
        self._new_password = new_password
        self._expert_level = expert_level
        self._codepostal = codepostal

    @classmethod
    def from_dict(cls, dikt) -> 'Changer':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Changer of this Changer.  # noqa: E501
        :rtype: Changer
        """
        return util.deserialize_model(dikt, cls)

    @property
    def pseudo(self) -> str:
        """Gets the pseudo of this Changer.


        :return: The pseudo of this Changer.
        :rtype: str
        """
        return self._pseudo

    @pseudo.setter
    def pseudo(self, pseudo: str):
        """Sets the pseudo of this Changer.


        :param pseudo: The pseudo of this Changer.
        :type pseudo: str
        """
        if pseudo is None:
            raise ValueError("Invalid value for `pseudo`, must not be `None`")  # noqa: E501

        self._pseudo = pseudo

    @property
    def password(self) -> str:
        """Gets the password of this Changer.


        :return: The password of this Changer.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password: str):
        """Sets the password of this Changer.


        :param password: The password of this Changer.
        :type password: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

    @property
    def new_password(self) -> str:
        """Gets the new_password of this Changer.


        :return: The new_password of this Changer.
        :rtype: str
        """
        return self._new_password

    @new_password.setter
    def new_password(self, new_password: str):
        """Sets the new_password of this Changer.


        :param new_password: The new_password of this Changer.
        :type new_password: str
        """

        self._new_password = new_password

    @property
    def expert_level(self) -> int:
        """Gets the expert_level of this Changer.


        :return: The expert_level of this Changer.
        :rtype: int
        """
        return self._expert_level

    @expert_level.setter
    def expert_level(self, expert_level: int):
        """Sets the expert_level of this Changer.


        :param expert_level: The expert_level of this Changer.
        :type expert_level: int
        """

        self._expert_level = expert_level

    @property
    def codepostal(self) -> int:
        """Gets the codepostal of this Changer.


        :return: The codepostal of this Changer.
        :rtype: int
        """
        return self._codepostal

    @codepostal.setter
    def codepostal(self, codepostal: int):
        """Sets the codepostal of this Changer.


        :param codepostal: The codepostal of this Changer.
        :type codepostal: int
        """

        self._codepostal = codepostal
