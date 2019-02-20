from flask import request
from flask import json
from flask import Response
from flask import Blueprint
from ..models.UserModel import UserModel
from ..models.UserModel import UserSchema
from ..shared.Authentication import Auth

validate_api = Blueprint('validate', __name__)
user_schema = UserSchema()


@validate_api.route('/', methods=['POST'])
def validate_token():
    """
    Create User Function (CREATE)
    """
    # Force is because I am not requesting application/json in the example html
    # https://stackoverflow.com/questions/20001229/how-to-get-posted-json-in-flask
    req_data = request.get_json(force=True)

    token = req_data["jwt"]
    data = Auth.decode_token(token)
    if data['error']:
        return Response(
            mimetype="application/json",
            response=json.dumps(data['error']),
            status=400
        )

    user_id = data['data']['user_id']
    user = UserModel.get_one_user(user_id)
    if not user:
        return custom_response({'error': 'user not found'}, 404)

    ser_user = user_schema.dump(user).data
    return custom_response({
        'message': 'Access granted.',
        'data': ser_user,
    }, 201)


def custom_response(res, status_code):
    """
    Custom response
    """
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )
