import itertools
from expressio import db
from gensim.models import Doc2Vec
import os
import re

MODELDIR = os.getcwd() + "/expressio/model/reddit_doc2vec.model"

model = Doc2Vec.load(MODELDIR)


def get_all_providers():
    r = db.engine.execute("SELECT DISTINCT provider_id, provider_name, provider_type FROM scorecard")
    vals = r.fetchall()
    return list(map(dict, vals))

def get_provider(provider_id):
    r = db.engine.execute("SELECT DISTINCT provider_id, provider_name, provider_type FROM scorecard WHERE provider_id=%d" % provider_id)
    vals = r.fetchall()
    return list(map(dict, vals))

def get_programs_for_provider(provider_id):
    r = db.engine.execute("SELECT DISTINCT program_cip, program_type FROM scorecard WHERE provider_id=%d" % provider_id)
    vals = r.fetchall()
    return list(map(dict, vals))

def get_outcomes_for_program(provider_id, program_id):
    r = db.engine.execute("SELECT * FROM scorecard WHERE provider_id=%d and program_cip=%d" % (provider_id, program_id))
    vals = r.fetchall()
    return list(map(dict, vals))

def find_most_similar_topic(post, topn):
    post = re.sub(r'\W+|\d+', ' ', post).lower().split()
    return model.docvecs.most_similar([model.infer_vector(post)], topn=topn)

def find_most_similar(word, topn):
    word = word.lower()
    return model.most_similar(word, topn=topn)
