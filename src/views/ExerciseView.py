from flask import request
from flask import json
from flask import Response
from flask import Blueprint
from flask import g

from ..models.ExerciseModel import ExerciseModel
from ..models.ExerciseModel import ExerciseSchema
from ..shared.Authentication import Auth

exercise_api = Blueprint('exercises', __name__)
exercise_schema = ExerciseSchema()


@exercise_api.route('/', methods=['POST'])
def create():
    """
    Create User Function (CREATE)
    """
    req_data = request.get_json()
    data, error = exercise_schema.load(req_data)

    if error:
        return custom_response(error, 400)

    exercise = ExerciseModel(data)
    exercise.save()

    # I am not sure if this is the correct response we want to provide
    # I just copied the code from UserView
    exercise_data = exercise_schema.dump(exercise).data
    token = Auth.generate_token(exercise_data.get('id'))

    return custom_response({'jwt_token': token}, 201)


@exercise_api.route('/', methods=['GET'])
@Auth.auth_required
def get_all():
    exercises = ExerciseModel.get_all_exercises()
    ser_exercises = exercise_schema.dump(exercises, many=True).data
    return custom_response(ser_exercises, 200)


@exercise_api.route('/<int:exercise_id>', methods=['GET'])
@Auth.auth_required
def get_a_exercise(exercise_id):
    exercise = ExerciseModel.get_one_exercise(exercise_id)
    if not exercise:
        return custom_response({'error': 'exercise not found'}, 404)

    ser_exercise = exercise_schema.dump(exercise).data
    return custom_response(ser_exercise, 200)


def custom_response(res, status_code):
    """
    Custom response
    """
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )
