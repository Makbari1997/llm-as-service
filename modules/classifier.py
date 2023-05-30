import numpy as np
from transformers import TFAutoModelForSequenceClassification, AutoTokenizer


class Classifier:
    def __init__(self, pretrained_path:str) -> None:
        self.model = TFAutoModelForSequenceClassification.from_pretrained(pretrained_path)
        self.tokenizer = AutoTokenizer.from_pretrained(pretrained_path)
        self.indx_to_lbl = {
            0: 'AddToPlaylist',
            1: 'PlayMusic',
            2: 'GetWeather',
            3: 'BookRestaurant',
            4: 'SearchCreativeWork',
            5: 'RateBook',
            6: 'SearchScreeningEvent',
        }
        self.max_length = 30

    def make_prediction(self, utterance:str) -> dict:
        utterance_tokenized = self.tokenizer(
            utterance, return_tensors='tf', padding='max_length', max_length=30, truncation=True
        )
        prediction = np.argmax(self.model(**utterance_tokenized)[0].numpy())
        return {'intent': self.indx_to_lbl[prediction]}