import pandas as pd
from pandas import DataFrame
import nltk
from blacksheep import Application
from blacksheep import status_code
from main import *

app = Application()

# docs = OpenAPIHandler(info=Info(title="Example API", version="0.0.1"))
# docs.bind_app(app)
df = pd.read_csv('spam.csv', encoding='ISO-8859-1')

# @app.route("/get_feature")
def get_feature(text):
    if len(text)==2:
        return {'ham':text[-3]}
        # return status_code(200, message={'ham':text[-3]})
    elif len(text)>=1:
        return {'spam':text[-3]}
        # return status_code(200, message={'spam':text[-3]})
    else:
        return {'ham':'', 'spam':''}
        # return status_code(200, message={'ham':'', 'spam':''})
# print(get_feature)
# return status_code(200, message={'message': msg})

# @app.route("/get_feature_text")
def get_feature_text(text):
    if len(text)==2:
        return {'spam':text[-2], 'ham':text[-1]} 
        # return status_code(200, message={'spam':text[-2], 'ham':text[-1]})
    else:
        return {'spam':DataFrame.rename(text[-2])[0], 'ham':DataFrame.rename(text[-1])[0]}
        # return status_code(200, message={'spam':DataFrame.rename(text[-2])[0], 'ham':DataFrame.rename(text[-1])[0]})

# @app.route("/get_data")
def get_data(df, get_feature=get_feature):
    featrues = []
    for i, row in df.iterrows():
        text = row['v1']; type = row['v2']
        if isinstance(text, str):
            if ' ' in text:
                text = text.replace(' ', '')
            if '(' not in text:
                featrues.append((get_feature(text), type.strip('() ')))
            else:
                text = text.partition('(')[0]
                featrues.append((get_feature(text), type.strip('() ')))
    return featrues
    # return status_code(200, message={'message': featrues})

# @app.route("/get_train_test")
def get_train_test(featrues, ratio=0.9):
    N = len(featrues)
    T = int(N * ratio)
    train = featrues[:T]
    test = featrues[T:]
    return train, test
    # return status_code(200, message={'message': (train, test)})

# @app.route("/text_classifier")
def text_classifier(df, f=get_feature):
    data = get_data(df, f)
    train, test = get_train_test(data)
    classifier = nltk.NaiveBayesClassifier.train(train)
    acc = nltk.classify.accuracy(classifier, test)
    return classifier, acc
    # return status_code(200, message={'message': (classifier, acc)})

@app.route("/show_type_of_text")
def show_type_of_text(text, texts=False, show_acc=False):
    f = get_feature_text if texts else get_feature
    classifier, acc = text_classifier(df, f)
    if show_acc:
        # print(f'Accuracy: {acc:.4}') 
        print("The accuracy of prediction is: ", acc)
    clf = classifier.classify(f(text))
    print(f'{text}: {clf}')
    classifier.show_most_informative_features(10)
    # return status_code(200, message={'message': classifier.show_most_informative_features(10)})
    return status_code(200, message={'message': f'{f}: {df}'})

# @docs(responses={200: "Returns a text saying OpenAPI Example"})
@app.route("/give_type")
def give_type(type1='spam', type2='ham'):
    data = get_data(df, get_feature)
    classifier = nltk.NaiveBayesClassifier.train(data)
    following = classifier.prob_classify({'ham':type2, 'spam':type1})
    x = following.generate()
    # print(f'{type2}: {type1}{x}')
    return status_code(200, message={'message': f'{type2}: {type1}{x}{data}'})

# if __name__ == '__main__':
#     print(give_type)
#     app.run()

# //////////////////////////////////////////////////////////
# import requests
# api_url = "https://nameless-mountain-71986.herokuapp.com/"
# response = requests.get(api_url)
# response.json()
# from datetime import datetime
# from blacksheep import Application


# app = Application()

# @app.route("/")
# def home():
    # return f"Hello, World! {datetime.utcnow().isoformat()}"
# //////////////////////////////////////
# if __name__ == '__main__':
#     print(df)

# /////////////////////////////////////////////////////////////////
# @app.route("/get_feature")
# def get_feature(text):
#     if len(text)==2:
#         # return {'ham':text[-3]}
#         return status_code(200, message={'ham':text[-3]})
#     elif len(text)>=1:
#         # return {'spam':text[-3]}
#         return status_code(200, message={'spam':text[-3]})
#     else:
#         # return {'ham':'', 'spam':''}
#         return status_code(200, message={'ham':'', 'spam':''})
# # print(get_feature)
# # return status_code(200, message={'message': msg})

# # @app.route("/get_feature_text")
# # def get_feature_text(text):
# #     if len(text)==2:
# #         # return {'spam':text[-2], 'ham':text[-1]} 
# #         return status_code(200, message={'spam':text[-2], 'ham':text[-1]})
# #     else:
# #         # return {'spam':DataFrame.rename(text[-2])[0], 'ham':DataFrame.rename(text[-1])[0]}
# #         return status_code(200, message={'spam':DataFrame.rename(text[-2])[0], 'ham':DataFrame.rename(text[-1])[0]})

# @app.route("/get_data")
# def get_data(df, get_feature=get_feature, ratio=0.9, f=get_feature):
#     featrues = []
#     for i, row in df.iterrows():
#         text = row['v1']; type = row['v2']
#         if isinstance(text, str):
#             if ' ' in text:
#                 text = text.replace(' ', '')
#             if '(' not in text:
#                 featrues.append((get_feature(text), type.strip('() ')))
#             else:
#                 text = text.partition('(')[0]
#                 featrues.append((get_feature(text), type.strip('() ')))
#     # ////////////////////////////////////////////////////////////////////////////////
#     # return featrues
#     N = len(featrues)
#     T = int(N * ratio)
#     train = featrues[:T]
#     test = featrues[T:]
#     # /////////////////////////////////////////////////////////////////////////////////
#     data = get_data(df, f)
#     train, test = get_data(data)
#     classifier = nltk.NaiveBayesClassifier.train(train)
#     acc = nltk.classify.accuracy(classifier, test)
#     return status_code(200, message={'message': (classifier, acc, featrues, train, test)})

# @app.route("/show_type_of_text")
# def show_type_of_text(text, texts=False, show_acc=False, type1='spam', type2='ham'):
#     f = get_data if texts else get_feature
#     classifier, acc = get_data(df, f)
#     if show_acc:
#         # print(f'Accuracy: {acc:.4}') 
#         print("The accuracy of prediction is: ", acc)
#     clf = classifier.classify(f(text))
#     print(f'{text}: {clf}')
#     classifier.show_most_informative_features(10)
#     # ////////////////////////////////////////////////////////////////////////////////
#     data = get_data(df, get_feature)
#     classifier = nltk.NaiveBayesClassifier.train(data)
#     following = classifier.prob_classify({'ham':type2, 'spam':type1})
#     x = following.generate()
#     print(f'{type2}: {type1}{x}')
#     msg = f"Pair Added"
#     return status_code(200, message={'message': msg})