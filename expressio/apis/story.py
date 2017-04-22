from flask_restplus import Namespace, Resource, fields
from expressio.database import model

api = Namespace('story', description='Story-related api')

@api.route('/<int:teller_id>/<int:story_id>')
@api.param('teller_id', 'The teller identifier')
@api.param('story_id', 'The story code')
@api.response(404, 'Program not found')
class Stories(Resource):
    @api.doc("get stories from a teller")
    def get(self, teller_id, story_id):
        '''Fetch all programs given the teller's identifier'''
        try:
            return model.get_outcomes_for_program(teller_id, program_id)
        except:
            api.abort(404)

@api.route('/<word>/get_similar/<int:topn>')
@api.param('word', 'texts')
@api.response(404, 'Word not found')
class Emotions(Resource):
    @api.doc("get emotions")
    def get(self, word, topn):
        try:
            word = word.lower()
            #print(model.find_most_similar(word, topn=topn))
            return model.find_most_similar(word, topn=topn)
        except:
            api.abort(404)

@api.route('/<story>/get_categories/<int:topn>')
@api.param('story', 'texts')
@api.response(404, 'Story not found')
class Categories(Resource):
    @api.doc("get categories")
    def get(self, story, topn):
        try:
            result = model.find_most_similar_topic(story, 10)
            return result
        except:
            api.abort(404)
