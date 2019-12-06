import connexion
import six
import mysql.connector


from swagger_server.models.changer import Changer  # noqa: E501
from swagger_server.models.info import Info  # noqa: E501
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
    conn = mysql.connector.connect(host="nuitinfo2.devling.net",user="ubuntu",password="ubuntu", database="nuitinfo")
    cursor = conn.cursor()
    try:
        cursor.execute("""INSERT INTO UserAccount (pseudo,password,codepostal,expertlevel) VALUES(%s,%s,%s,%s)""",(body.pseudo, body.password, body.codepostal, body.expert_level))
        conn.commit()
    except Exception as e:
        return "{ \"Message\" : \"Désolé, ce pseudo est déjà pris.\" }"

    conn.close()
    return "{ \"Message\" : \"Done\" }"

def get_user(pseudo, password):  # noqa: E501
    """Getting informations from a user

     # noqa: E501

    :param pseudo:
    :type pseudo: str
    :param password:
    :type password: str

    :rtype: Info
    """
    conn = mysql.connector.connect(host="nuitinfo2.devling.net",user="ubuntu",password="ubuntu", database="nuitinfo")
    cursor = conn.cursor()
    try:
        cursor.execute("""SELECT codepostal, expertlevel FROM UserAccount WHERE pseudo = %s AND password = %s""", (pseudo, password))
        rows = cursor.fetchall()
        codepostal = rows[0][0]
        expert_level = rows[0][1]
    except Exception as e:
        return "{ \"Message\" : \"Utilisateur non trouvé.\" }"

    conn.close()
    return "{ \"codepostal\" : \"" + str(codepostal) + ",\"expert_level\" : \"" + str(expert_level) + "\" }"


def login(body):  # noqa: E501
    """Check for valid user pseudo and password

     # noqa: E501

    :param body: log in a user
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Login.from_dict(connexion.request.get_json())  # noqa: E501
    conn = mysql.connector.connect(host="nuitinfo2.devling.net",user="ubuntu",password="ubuntu", database="nuitinfo")
    cursor = conn.cursor()
    try:
        cursor.execute("""SELECT * FROM UserAccount WHERE pseudo = %s AND password = %s""", (body.pseudo, body.password))
    except Exception as e:
        return "{ \"Message\" : \"Utilisateur non trouvé.\" }"

    conn.close()
    return "{ \"Message\" : \"Connexion réussie.\" }"


def put_user(Changer2=None):  # noqa: E501
    """Changing user information

     # noqa: E501

    :param Changer:
    :type Changer: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        Changer2 = Changer.from_dict(connexion.request.get_json())  # noqa: E501
    conn = mysql.connector.connect(host="nuitinfo2.devling.net",user="ubuntu",password="ubuntu", database="nuitinfo")
    cursor = conn.cursor()
    try:
        cursor.execute("""SELECT * FROM UserAccount WHERE pseudo = %s AND password = %s""", (Changer2.pseudo, Changer2.password))
        rows = cursor.fetchall()
        if(rows == []):
            return "{ \"Message\" : \"Utilisateur non trouvé.\" }"
        if(Changer2.codepostal is not None):
            cursor.execute("""UPDATE UserAccount SET codepostal = %s WHERE pseudo = %s AND password = %s""", (Changer2.codepostal,Changer2.pseudo,Changer2.password))
        if(Changer2.new_password is not None):
            cursor.execute("""UPDATE UserAccount SET password = %s WHERE pseudo = %s AND password = %s""", (Changer2.new_password,Changer2.pseudo,Changer2.password))
        if(Changer2.expert_level is not None):
            cursor.execute("""UPDATE UserAccount SET expertlevel = %s WHERE pseudo = %s AND password = %s""", (Changer2.expert_level,Changer2.pseudo,Changer2.password))
        conn.commit()
    except Exception as e:
        return "{ \"Message\" : \"Utilisateur non trouvé.\" }"

    conn.close()
    return "{ \"Message\" : \"Changements effectués.\" }"
