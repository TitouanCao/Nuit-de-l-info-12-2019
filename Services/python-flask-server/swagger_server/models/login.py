# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Login(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, pseudo: str=None, password: str=None):  # noqa: E501
        """Login - a model defined in Swagger

        :param pseudo: The pseudo of this Login.  # noqa: E501
        :type pseudo: str
        :param password: The password of this Login.  # noqa: E501
        :type password: str
        """
        self.swagger_types = {
            'pseudo': str,
            'password': str
        }

        self.attribute_map = {
            'pseudo': 'pseudo',
            'password': 'password'
        }

        self._pseudo = pseudo
        self._password = password

    @classmethod
    def from_dict(cls, dikt) -> 'Login':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Login of this Login.  # noqa: E501
        :rtype: Login
        """
        return util.deserialize_model(dikt, cls)

    @property
    def pseudo(self) -> str:
        """Gets the pseudo of this Login.


        :return: The pseudo of this Login.
        :rtype: str
        """
        return self._pseudo

    @pseudo.setter
    def pseudo(self, pseudo: str):
        """Sets the pseudo of this Login.


        :param pseudo: The pseudo of this Login.
        :type pseudo: str
        """
        if pseudo is None:
            raise ValueError("Invalid value for `pseudo`, must not be `None`")  # noqa: E501

        self._pseudo = pseudo

    @property
    def password(self) -> str:
        """Gets the password of this Login.


        :return: The password of this Login.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password: str):
        """Sets the password of this Login.


        :param password: The password of this Login.
        :type password: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password
