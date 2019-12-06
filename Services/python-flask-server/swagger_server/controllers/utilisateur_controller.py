import connexion
import six

from swagger_server.models.changer import Changer  # noqa: E501
from swagger_server.models.login import Login  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server import util


def add_user(body):  # noqa: E501
    """Add a new user to the site

     # noqa: E501

    :param body: New User that need to be added to the data base
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_user(pseudo, password, expert_level, codepostal):  # noqa: E501
    """Getting informations from a user

     # noqa: E501

    :param pseudo: 
    :type pseudo: str
    :param password: 
    :type password: str
    :param expert_level: 
    :type expert_level: int
    :param codepostal: 
    :type codepostal: int

    :rtype: None
    """
    return 'do some magic!'


def login(body):  # noqa: E501
    """Check for valid user pseudo and password

     # noqa: E501

    :param body: log in a user
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Login.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def put_user(Changer=None):  # noqa: E501
    """Changing user information

     # noqa: E501

    :param Changer: 
    :type Changer: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        Changer = Changer.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
