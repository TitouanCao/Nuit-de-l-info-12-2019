# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.changer import Changer  # noqa: E501
from swagger_server.models.info import Info  # noqa: E501
from swagger_server.models.login import Login  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server.test import BaseTestCase


class TestUtilisateurController(BaseTestCase):
    """UtilisateurController integration test stubs"""

    def test_add_user(self):
        """Test case for add_user

        Add a new user to the site
        """
        body = User()
        response = self.client.open(
            '/compte/Utilisateur/register',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_user(self):
        """Test case for get_user

        Getting informations from a user
        """
        query_string = [('pseudo', 'pseudo_example'),
                        ('password', 'password_example')]
        response = self.client.open(
            '/compte/Utilisateur/info',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_login(self):
        """Test case for login

        Check for valid user pseudo and password
        """
        body = Login()
        response = self.client.open(
            '/compte/Utilisateur/login',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_user(self):
        """Test case for put_user

        Changing user information
        """
        Changer = Changer()
        response = self.client.open(
            '/compte/Utilisateur/info',
            method='POST',
            data=json.dumps(Changer),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
