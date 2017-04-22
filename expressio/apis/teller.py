from flask_restplus import Namespace, Resource, fields
from expressio.database import model

api = Namespace('teller', description='Story teller related api')

provider = api.model('Teller', {
    'teller_id': fields.String(required=True, description='The teller identifier'),
    'teller_name': fields.String(required=True, description='The teller name'),
    'teller_type': fields.String(required=True, description='The teller type'),
    })


@api.route('/')
class TellerList(Resource):
    @api.doc('list_tellers')
    #@api.marshal_list_with(provider)
    def get(self):
        '''
        List all tellers
        '''
        #return model.get_all_providers()
        return [['Rose','1021']]

@api.route('/<int:id>')
@api.param('id', 'The teller identifier')
@api.response(404, 'Teller not found')
class tellers(Resource):
    @api.doc('get tellers')
    @api.marshal_list_with(provider)
    def get(self, id):
        '''Fetch a teller given its identifier'''
        try:
            return model.get_provider(id)
        except:
            api.abort(404)
