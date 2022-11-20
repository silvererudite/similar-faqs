from peewee import Model, SqliteDatabase, CharField, TextField
db = SqliteDatabase('faqs.db')

class FaqModel(Model):
  query = TextField()
  possibleAnswer = TextField(null=True)

  class Meta:
    database = db

db.create_tables([FaqModel])