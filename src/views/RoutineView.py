from flask import request
from flask import json
from flask import Response
from flask import Blueprint


from ..models.RoutineModel import RoutineModel
from ..models.RoutineModel import RoutineSchema
from ..models.ExerciseModel import ExerciseModel
from ..models.ExerciseModel import ExerciseSchema
from ..shared.Authentication import Auth

routine_api = Blueprint('routines', __name__)
routine_schema = RoutineSchema()


@routine_api.route('/', methods=['POST'])
def create():
    """
    Create User Function (CREATE)
    """
    req_data = request.get_json()
    data, error = routine_schema.load(req_data)

    if error:
        return custom_response(error, 400)

    exercises_object = []
    exercises = data.get('exercises', {})
    for exercise in exercises:
        exercise_in_db = ExerciseModel.get_exercise_by_name(
            exercise.get("name")
        )

        if not exercise_in_db:
            message = {
                'error': 'Exercise {} not found in the DB'.format(
                    exercise.get("name")
                )
            }
            return custom_response(message, 400)

        exercises_object.append(exercise_in_db)

    routine = RoutineModel(data)
    routine.exercises = exercises_object
    routine.save()

    # I am not sure if this is the correct response we want to provide
    # I just copied the code from UserView
    routine_data = routine_schema.dump(routine).data
    token = Auth.generate_token(routine_data.get('id'))

    return custom_response({'jwt_token': token}, 201)


@routine_api.route('/', methods=['GET'])
@Auth.auth_required
def get_all():
    routines = RoutineModel.get_all_routines()
    ser_routines = routine_schema.dump(routines, many=True).data
    return custom_response(ser_routines, 200)


@routine_api.route('/<int:routine_id>', methods=['GET'])
@Auth.auth_required
def get_a_routine(routine_id):
    routine = RoutineModel.get_one_routine(routine_id)
    if not routine:
        return custom_response({'error': 'routine not found'}, 404)

    ser_routine = routine_schema.dump(routine).data
    return custom_response(ser_routine, 200)


def custom_response(res, status_code):
    """
    Custom response
    """
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )
