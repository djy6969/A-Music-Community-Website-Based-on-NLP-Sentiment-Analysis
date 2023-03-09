import json
import pandas as pd
from paddlenlp import Taskflow


def read_comment_json(filepath):
    out = []
    with open(filepath) as f:
        data = json.load(f)
    for item in data:
        if item['comment'] != '':
            out.append(item)
    return out


def json_to_dataframe(data):
    dataDF = pd.DataFrame(data)
    return dataDF


def sentient_score(data):
    senta = Taskflow("sentiment_analysis")
    for item in data:
        item['label'] = senta(item['comment'])[0]['label']
        item['score'] = senta(item['comment'])[0]['score']
    return data


def get_positive_top(data_df, rank):
    positiveDF = data_df[data_df['label'].isin(["positive"])]
    js = positiveDF.sort_values(by=['score'], ascending=False).head(rank).to_json(orient='records')
    return js


def get_negative_top(data_df, rank):
    negativeDF = data_df[data_df['label'].isin(["negative"])]
    js = negativeDF.sort_values(by=['score'], ascending=False).head(rank).to_json(orient='records')
    return js


# input some text
# output is the score of the text
def sentient_analysis(txt):
    senta = Taskflow("sentiment_analysis")
    result = senta(txt)
    return result


def text_correction(txt):
    senta = Taskflow("text_correction")
    result = senta(txt)
    return result


json_file = read_comment_json('test_comments1.json')
json_file = sentient_score(json_file)
df = json_to_dataframe(json_file)
json_top = get_positive_top(df, 10)
json_bottom = get_negative_top(df, 10)
