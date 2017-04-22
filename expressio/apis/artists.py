from flask_restplus import Namespace, Resource, fields
from expressio.database import model

api = Namespace('artist', description='Artist related apis')

artist = api.model('Artist', {
    'artist_cip': fields.String(required=True, description='The artist code'),
    'artist_type': fields.String(required=True, description='The artist emotion type'),
    })


@api.route('/<int:artist_id>')
@api.param('artist_id', 'The artist identifier')
@api.response(404, 'Program not found')
class Program(Resource):
    @api.doc('get all programs from the provider')
    @api.marshal_list_with(program)
    def get(self, provider_id):
        '''Fetch all programs given the provider's identifier'''
        try:
            return model.get_programs_for_provider(provider_id)
        except:
            api.abort(404)
