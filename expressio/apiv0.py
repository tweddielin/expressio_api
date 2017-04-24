from flask import Blueprint
from flask_restplus import Api

from .apis.teller import api as teller
from .apis.artist import api as artist
from .apis.story import api as story
from .apis.track import api as track

blueprint = Blueprint('api', __name__, url_prefix='/api/v0')
api = Api(blueprint,
        title='Expressivo',
        version='0.1',
        description='API service for connecting story-tellers, artists and audience together.'
        )

api.add_namespace(teller)
api.add_namespace(artist)
api.add_namespace(story)
api.add_namespace(track)
