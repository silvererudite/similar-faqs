from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel, validator

import tasks

app = FastAPI()

class FaqQuery(BaseModel):
  text: str

@app.get("/")
def get_root():
  return {"message": "Hello world"}

@app.post("/query")
def post_query(q: FaqQuery, background_tasks: BackgroundTasks):
  # store the query
  # run sentence similarity in abckground
  q_id = tasks.store_query(q)
  background_tasks.add_task(tasks.get_answer, q_id)
  return {"task_id": q_id}

@app.get("/result")
def get_answer(q_id: int):
  return {"answer": tasks.show_result(q_id)}