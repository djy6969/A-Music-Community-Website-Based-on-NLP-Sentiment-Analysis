from transformers import AutoModelForSequenceClassification, AutoTokenizer, AutoConfig
from scipy.special import softmax
import numpy as np

PRECESS_STATE = 1
# MODEL = '/home/student/comp3032j/nlp/best_model'


def model_creation(model_path):
    global model, tokenizer, config
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    config = AutoConfig.from_pretrained(model_path)
    model = AutoModelForSequenceClassification.from_pretrained(model_path)
    

# Preprocess text (username and link placeholders)
def preprocess(text):
    new_text = []
    for t in text.split(" "):
        t = '@user' if t.startswith('@') and len(t) > 1 else t
        t = 'http' if t.startswith('http') else t
        new_text.append(t)
    return " ".join(new_text)


def predict(text):
    text = preprocess(text)
    encoded_input = tokenizer(text, return_tensors='pt')
    output = model(**encoded_input)
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)

    # Print labels and scores
    ranking = np.argsort(scores)
    ranking = ranking[::-1]
    for i in range(scores.shape[0]):
        l = config.id2label[ranking[i]]
        # s = scores[ranking[i]]
        print(l)
        return l

        # print(f"{i + 1}) {l} {np.round(float(s), 4)}")


# while PRECESS_STATE == 1:
#     text = input("Sentence for sentiment analysis, shown by positive, neutral or negative:")
#     predict(text)


# if __name__ == "__main__":
    # model_creation('/home/student/comp3032j/nlp/best_model')
    # while True:
    #     text = input("Sentence for sentiment analysis, shown by positive, neutral or negative:")
    #     predict(text)
    
