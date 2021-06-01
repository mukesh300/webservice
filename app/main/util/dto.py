from flask_restplus import Namespace, fields


class User:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address', example='xyz@abc.com'),
        'username': fields.String(required=True, description='user username', example='xyz'),
        'password': fields.String(required=True, description='user password', example='my_password'),
        'public_id': fields.String(description='user Identifier')
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })
