import uvicorn
import logging
from pydantic import BaseModel
from classifier import Classifier
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

logging.basicConfig(level = logging.INFO)


app = FastAPI()
templates = Jinja2Templates(directory="templates")
classifier = Classifier('./roberta-finetuned/')

class Utterance(BaseModel):
    utterance: str

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/intent_detection")
async def intent_detection(utterance: Utterance):
    try:
        utterance_str = utterance.utterance
        result = classifier.make_prediction(utterance_str)
        return result
    except Exception as e:
        logging.error('Something went wrong')


if __name__ == '__main__':
    uvicorn.run('app:app', reload=True, port=8000, host='0.0.0.0')