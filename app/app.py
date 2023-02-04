from fastapi import FastAPI, HTTPException
import uvicorn
from app.main import unique_letter

app = FastAPI()


@app.get('/')
async def root():
    return {'status': 'Working'}


@app.post('/home/')
async def result(text: str):
    res = unique_letter(text)
    if res is not None:
        return unique_letter(text)
    else:
        raise HTTPException(status_code=404, detail='No unique letter was found')


if __name__ == '__main__':
    uvicorn.run('app:app', host='localhost', reload=True, port=8000)
