from models import FaqModel
import numpy as np # linear algebra
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
import pickle

with open('embeddings.pkl', "rb") as fIn:
    stored_data = pickle.load(fIn)
    embeddings = stored_data['embeddings']

with open('answers.pkl', "rb") as fIn:
    stored_data = pickle.load(fIn)
    answers = stored_data['answers']

embedder = SentenceTransformer('msmarco-MiniLM-L-6-v3')
def store_query(q):
  model = FaqModel(query = q.text)
  model.save()
  return model.id

def get_answer(q_id: int):
  model = FaqModel.get_by_id(q_id)
  embeded_ques = embedder.encode(model.query)
  em_vec = np.vstack([embeded_ques]*10)
  scores = cosine_similarity(embeddings, em_vec)
  idx = np.argmax([np.mean(arr) for arr in scores])
  model.possibleAnswer = answers[idx]
  model.save()

def show_result(q_id: int):
  model = FaqModel.get_by_id(q_id)

  answer = model.possibleAnswer
  if answer is None:
    answer = "Processing..."
  return answer 

