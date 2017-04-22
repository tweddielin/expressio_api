from flask_restplus import Namespace, Resource, fields
from expressio.database import model

api = Namespace('track', description='Track related apis')

track = api.model('Track', {
    'track_cip': fields.String(required=True, description='The track code'),
    'track_type': fields.String(required=True, description='The track emotion type'),
    })


@api.route('/<int:track_id>')
@api.param('track_id', 'The track identifier')
@api.response(404, 'Program not found')
class Track(Resource):
    @api.doc('get all programs from the provider')
    def get(self, track_id):
        '''Fetch all programs given the provider's identifier'''
        try:
            #return model.get_programs_for_provider(provider_id)
            return [['radiohead', 'high and dry']]
        except:
            api.abort(404)

@api.route('/<int:track_id>/get_emotion')
@api.param('track_id', 'texts')
@api.response(404, 'Word not found')
class Emotions(Resource):
    @api.doc("get emotions")
    def get(self, track_id):
        try:
            #word = word.lower()
            #print(model.find_most_similar(word, topn=topn))
            #return model.find_most_similar(word, topn=topn)
            return ['sad', 'confused', 'lost']
        except:
            api.abort(404)
