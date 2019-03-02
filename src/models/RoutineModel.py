from . import db
import datetime
from marshmallow import fields, Schema
from .ExerciseModel import ExerciseSchema

association_table = db.Table(
    'association', db.Model.metadata,
    db.Column('routine_id', db.Integer, db.ForeignKey('routines.id')),
    db.Column('exercise_id', db.Integer, db.ForeignKey('exercises.id'))
)


class RoutineModel(db.Model):
    """
    Routine Model
    """

    __tablename__ = "routines"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)
    exercises = db.relationship(
        'ExerciseModel', secondary=association_table
    )

    def __init__(self, data):
        self.title = data.get('title')
        self.description = data.get('description')
        self.created_at = datetime.datetime.utcnow()
        self.modified_at = datetime.datetime.utcnow()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        self.modified_at = datetime.datetime.utcnow()
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all_routines():
        return RoutineModel.query.all()

    @staticmethod
    def get_one_routine(id):
        return RoutineModel.query.get(id)

    def __repr__(self):
        return '<id {}>'.format(self.id)


class RoutineSchema(Schema):
    """
    Question Schema
    """
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)
    modified_at = fields.DateTime(dump_only=True)
    exercises = fields.Nested(ExerciseSchema, many=True)
