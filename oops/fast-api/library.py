
from fastapi import FastAPI,HTTPException,status
# from pydantic import BaseModel
from model import Lib

app=FastAPI()


books=[{'id':1,'title':'harry potter','author':'jk rowling'},{'id':2,'title':'akosk','author':'george martin'}]

@app.get('/')
def home():
    return 'welcome to homepage library'

@app.post('/book',status_code=status.HTTP_201_CREATED)
def add_books(book:Lib):
    new=book.model_dump()
    books.append(new)

    return {'message':'new book created'}
@app.get('/book')
def get_books():
    return books
@app.put('/book/{id}')
def update(id:int,book:Lib):
    for b in books:
        if b['id']==id:
            b.update(book.model_dump())
            return books
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail={'message':'id not found'})

