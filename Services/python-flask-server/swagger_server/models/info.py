# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Info(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, expert_level: int=None, codepostal: int=None):  # noqa: E501
        """Info - a model defined in Swagger

        :param expert_level: The expert_level of this Info.  # noqa: E501
        :type expert_level: int
        :param codepostal: The codepostal of this Info.  # noqa: E501
        :type codepostal: int
        """
        self.swagger_types = {
            'expert_level': int,
            'codepostal': int
        }

        self.attribute_map = {
            'expert_level': 'expert_level',
            'codepostal': 'codepostal'
        }

        self._expert_level = expert_level
        self._codepostal = codepostal

    @classmethod
    def from_dict(cls, dikt) -> 'Info':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Info of this Info.  # noqa: E501
        :rtype: Info
        """
        return util.deserialize_model(dikt, cls)

    @property
    def expert_level(self) -> int:
        """Gets the expert_level of this Info.


        :return: The expert_level of this Info.
        :rtype: int
        """
        return self._expert_level

    @expert_level.setter
    def expert_level(self, expert_level: int):
        """Sets the expert_level of this Info.


        :param expert_level: The expert_level of this Info.
        :type expert_level: int
        """
        if expert_level is None:
            raise ValueError("Invalid value for `expert_level`, must not be `None`")  # noqa: E501

        self._expert_level = expert_level

    @property
    def codepostal(self) -> int:
        """Gets the codepostal of this Info.


        :return: The codepostal of this Info.
        :rtype: int
        """
        return self._codepostal

    @codepostal.setter
    def codepostal(self, codepostal: int):
        """Sets the codepostal of this Info.


        :param codepostal: The codepostal of this Info.
        :type codepostal: int
        """
        if codepostal is None:
            raise ValueError("Invalid value for `codepostal`, must not be `None`")  # noqa: E501

        self._codepostal = codepostal
