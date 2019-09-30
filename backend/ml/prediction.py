# coding: utf-8

import pandas as pd
import pandas
import pprint
from gensim.models import word2vec
import codecs
import numpy as np
import codecs
import shutil
import os
import pymorphy2
import seaborn as sns
from pandas import read_csv
import re
import gensim.downloader as api

from sklearn.cluster import KMeans
from sklearn.manifold import TSNE
from sklearn.preprocessing import normalize
import numpy as np

from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler

from matplotlib import pyplot as plt

from sklearn.decomposition import PCA

from sklearn.cluster import MeanShift
import json

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.linear_model import LogisticRegression

from sklearn.utils import shuffle

from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.model_selection import cross_val_score


def load_mashine():
    df_charity = pandas.read_json('backend/ml/charity.json', encoding='utf-8')
    df_animals = pandas.read_json('backend/ml/animals.json', encoding='utf-8')
    df_education = pandas.read_json('backend/ml/education.json', encoding='utf-8')
    df_healthy = pandas.read_json('backend/ml/healthy.json', encoding='utf-8')
    df_culture = pandas.read_json('backend/ml/culture.json', encoding='utf-8')

    df_charity = df_charity.drop('career', 1)
    df_charity = df_charity.drop('country', 1)
    df_charity = df_charity.drop('occupation', 1)

    df_animals = df_animals.drop('career', 1)
    df_animals = df_animals.drop('country', 1)
    df_animals = df_animals.drop('occupation', 1)

    df_education = df_education.drop('career', 1)
    df_education = df_education.drop('country', 1)
    df_education = df_education.drop('occupation', 1)

    df_healthy = df_healthy.drop('career', 1)
    df_healthy = df_healthy.drop('country', 1)
    df_healthy = df_healthy.drop('occupation', 1)

    df_culture = df_culture.drop('career', 1)
    df_culture = df_culture.drop('country', 1)
    df_culture = df_culture.drop('occupation', 1)

    df_charity = df_charity.drop_duplicates()
    df_animals = df_animals.drop_duplicates()
    df_education = df_education.drop_duplicates()
    df_healthy = df_healthy.drop_duplicates()
    df_culture = df_culture.drop_duplicates()

    df_charity['label_charity'] = 1
    df_charity['label_animals'] = 0
    df_charity['label_education'] = 0
    df_charity['label_healthy'] = 0
    df_charity['label_culture'] = 0

    df_charity['label_charity_score'] = np.random.randint(50, 100, size=len(df_charity))
    df_charity['label_animals_score'] = np.random.randint(0, 10, size=len(df_charity))
    df_charity['label_education_score'] = np.random.randint(0, 10, size=len(df_charity))
    df_charity['label_healthy_score'] = np.random.randint(0, 10, size=len(df_charity))
    df_charity['label_culture_score'] = np.random.randint(0, 10, size=len(df_charity))

    df_animals['label_charity'] = 0
    df_animals['label_animals'] = 1
    df_animals['label_education'] = 0
    df_animals['label_healthy'] = 0
    df_animals['label_culture'] = 0

    df_animals['label_charity_score'] = np.random.randint(0, 10, size=len(df_animals))
    df_animals['label_animals_score'] = np.random.randint(50, 100, size=len(df_animals))
    df_animals['label_education_score'] = np.random.randint(0, 10, size=len(df_animals))
    df_animals['label_healthy_score'] = np.random.randint(0, 10, size=len(df_animals))
    df_animals['label_culture_score'] = np.random.randint(0, 10, size=len(df_animals))

    df_education['label_charity'] = 0
    df_education['label_animals'] = 0
    df_education['label_education'] = 1
    df_education['label_healthy'] = 0
    df_education['label_culture'] = 0

    df_education['label_charity_score'] = np.random.randint(0, 10, size=len(df_education))
    df_education['label_animals_score'] = np.random.randint(0, 10, size=len(df_education))
    df_education['label_education_score'] = np.random.randint(50, 100, size=len(df_education))
    df_education['label_healthy_score'] = np.random.randint(0, 10, size=len(df_education))
    df_education['label_culture_score'] = np.random.randint(0, 10, size=len(df_education))

    df_healthy['label_charity'] = 0
    df_healthy['label_animals'] = 0
    df_healthy['label_education'] = 0
    df_healthy['label_healthy'] = 1
    df_healthy['label_culture'] = 0

    df_healthy['label_charity_score'] = np.random.randint(0, 10, size=len(df_healthy))
    df_healthy['label_animals_score'] = np.random.randint(0, 10, size=len(df_healthy))
    df_healthy['label_education_score'] = np.random.randint(0, 10, size=len(df_healthy))
    df_healthy['label_healthy_score'] = np.random.randint(50, 100, size=len(df_healthy))
    df_healthy['label_culture_score'] = np.random.randint(0, 10, size=len(df_healthy))

    df_culture['label_charity'] = 0
    df_culture['label_animals'] = 0
    df_culture['label_education'] = 0
    df_culture['label_healthy'] = 0
    df_culture['label_culture'] = 1

    df_culture['label_charity_score'] = np.random.randint(0, 10, size=len(df_culture))
    df_culture['label_animals_score'] = np.random.randint(0, 10, size=len(df_culture))
    df_culture['label_education_score'] = np.random.randint(0, 10, size=len(df_culture))
    df_culture['label_healthy_score'] = np.random.randint(0, 10, size=len(df_culture))
    df_culture['label_culture_score'] = np.random.randint(50, 100, size=len(df_culture))

    df_charity.to_csv('df_charity.CSV', encoding='utf-8')
    df_animals.to_csv('df_animals.CSV', encoding='utf-8')
    df_education.to_csv('df_education.CSV', encoding='utf-8')
    df_healthy.to_csv('df_healthy.CSV', encoding='utf-8')
    df_culture.to_csv('df_culture.CSV', encoding='utf-8')

    df_charity = pd.read_csv('df_charity.CSV', encoding='utf-8')
    df_animals = pd.read_csv('df_animals.CSV', encoding='utf-8')
    df_education = pd.read_csv('df_education.CSV', encoding='utf-8')
    df_healthy = pd.read_csv('df_healthy.CSV', encoding='utf-8')
    df_culture = pd.read_csv('df_culture.CSV', encoding='utf-8')

    df_charity = df_charity.drop('Unnamed: 0', 1)
    df_animals = df_animals.drop('Unnamed: 0', 1)
    df_education = df_education.drop('Unnamed: 0', 1)
    df_healthy = df_healthy.drop('Unnamed: 0', 1)
    df_culture = df_culture.drop('Unnamed: 0', 1)

    df_charity.replace(np.nan, 0, inplace=True)
    df_animals.replace(np.nan, 0, inplace=True)
    df_education.replace(np.nan, 0, inplace=True)
    df_healthy.replace(np.nan, 0, inplace=True)
    df_culture.replace(np.nan, 0, inplace=True)

    frames = [df_charity, df_animals, df_education, df_healthy, df_culture]
    df_drop = pd.concat(frames)
    df_drop = shuffle(df_drop)


    # CHARITY MODEL
    feature_cols = ['followers_count', 'has_mobile', 'has_photo', 'label_charity_score', 'label_animals_score',
                    'label_education_score', 'label_healthy_score', 'label_culture_score']
    labels_cols = ['label_charity']
    X = df_drop[feature_cols]
    Y = df_drop[labels_cols]

    split = int(0.7 * len(df_drop))
    X_train, X_test, Y_train, Y_test = X[:split], X[split:], Y[:split], Y[split:]

    charity_model_perfect = LogisticRegression()
    charity_model_perfect = charity_model_perfect.fit(X_train, Y_train)

    result_charity_perfect = charity_model_perfect.predict_proba(X_test)
    result_charity_perfect = pd.DataFrame(result_charity_perfect)


    feature_cols = ['followers_count', 'has_mobile', 'has_photo']
    labels_cols = ['label_charity']
    X = df_drop[feature_cols]
    Y = df_drop[labels_cols]

    split = int(0.7 * len(df_drop))
    X_train, X_test, Y_train, Y_test = X[:split], X[split:], Y[:split], Y[split:]

    charity_model_bad = LogisticRegression()
    charity_model_bad = charity_model_bad.fit(X_train, Y_train)

    result_charity_bad = charity_model_bad.predict_proba(X_test)
    result_charity_bad = pd.DataFrame(result_charity_bad)


    # ANIMALS
    feature_cols = ['followers_count', 'has_mobile', 'has_photo', 'label_charity_score', 'label_animals_score',
                    'label_education_score', 'label_healthy_score', 'label_culture_score']
    labels_cols = ['label_animals']
    X = df_drop[feature_cols]
    Y = df_drop[labels_cols]

    split = int(0.7 * len(df_drop))
    X_train, X_test, Y_train, Y_test = X[:split], X[split:], Y[:split], Y[split:]

    animals_model_perfect = LogisticRegression()
    animals_model_perfect = animals_model_perfect.fit(X_train, Y_train)

    result_animals_perfect = animals_model_perfect.predict_proba(X_test)
    result_animals_perfect = pd.DataFrame(result_animals_perfect)


    feature_cols = ['followers_count', 'has_mobile', 'has_photo']
    labels_cols = ['label_animals']
    X = df_drop[feature_cols]
    Y = df_drop[labels_cols]

    split = int(0.7 * len(df_drop))
    X_train, X_test, Y_train, Y_test = X[:split], X[split:], Y[:split], Y[split:]

    animals_model_bad = LogisticRegression()
    animals_model_bad = animals_model_bad.fit(X_train, Y_train)

    result_animals_bad = animals_model_bad.predict_proba(X_test)
    result_animals_bad = pd.DataFrame(result_animals_bad)


    # EDUCATION
    feature_cols = ['followers_count', 'has_mobile', 'has_photo', 'label_charity_score', 'label_animals_score',
                    'label_education_score', 'label_healthy_score', 'label_culture_score']
    labels_cols = ['label_education']
    X = df_drop[feature_cols]
    Y = df_drop[labels_cols]

    split = int(0.7 * len(df_drop))
    X_train, X_test, Y_train, Y_test = X[:split], X[split:], Y[:split], Y[split:]

    education_model_perfect = LogisticRegression()
    education_model_perfect = education_model_perfect.fit(X_train, Y_train)

    result_education_perfect = education_model_perfect.predict_proba(X_test)
    result_education_perfect = pd.DataFrame(result_education_perfect)


    feature_cols = ['followers_count', 'has_mobile', 'has_photo']
    labels_cols = ['label_education']
    X = df_drop[feature_cols]
    Y = df_drop[labels_cols]

    split = int(0.7*len(df_drop))
    X_train, X_test, Y_train, Y_test = X[:split], X[split:], Y[:split], Y[split:]

    education_model_bad = LogisticRegression()
    education_model_bad = education_model_bad.fit(X_train, Y_train)

    result_education_bad = education_model_bad.predict_proba(X_test)
    result_education_bad = pd.DataFrame(result_education_bad)


    # HEALTHY
    feature_cols = ['followers_count', 'has_mobile', 'has_photo', 'label_charity_score', 'label_animals_score',
                    'label_education_score', 'label_healthy_score', 'label_culture_score']
    labels_cols = ['label_healthy']
    X = df_drop[feature_cols]
    Y = df_drop[labels_cols]

    split = int(0.7 * len(df_drop))
    X_train, X_test, Y_train, Y_test = X[:split], X[split:], Y[:split], Y[split:]

    healthy_model_perfect = LogisticRegression()
    healthy_model_perfect = healthy_model_perfect.fit(X_train, Y_train)

    result_healthy_perfect = healthy_model_perfect.predict_proba(X_test)
    result_healthy_perfect = pd.DataFrame(result_healthy_perfect)


    feature_cols = ['followers_count', 'has_mobile', 'has_photo']
    labels_cols = ['label_healthy']
    X = df_drop[feature_cols]
    Y = df_drop[labels_cols]

    split = int(0.7 * len(df_drop))
    X_train, X_test, Y_train, Y_test = X[:split], X[split:], Y[:split], Y[split:]

    healthy_model_bad = LogisticRegression()
    healthy_model_bad = healthy_model_bad.fit(X_train, Y_train)

    result_healthy_bad = healthy_model_bad.predict_proba(X_test)
    result_healthy_bad = pd.DataFrame(result_healthy_bad)


    # CULTURE
    feature_cols = ['followers_count', 'has_mobile', 'has_photo', 'label_charity_score', 'label_animals_score',
                    'label_education_score', 'label_healthy_score', 'label_culture_score']
    labels_cols = ['label_culture']
    X = df_drop[feature_cols]
    Y = df_drop[labels_cols]

    split = int(0.7 * len(df_drop))
    X_train, X_test, Y_train, Y_test = X[:split], X[split:], Y[:split], Y[split:]

    culture_model_perfect = LogisticRegression()
    culture_model_perfect = culture_model_perfect.fit(X_train, Y_train)

    result_culture_perfect = culture_model_perfect.predict_proba(X_test)
    result_culture_perfect = pd.DataFrame(result_culture_perfect)

    feature_cols = ['followers_count', 'has_mobile', 'has_photo']
    labels_cols = ['label_culture']
    X = df_drop[feature_cols]
    Y = df_drop[labels_cols]

    split = int(0.7 * len(df_drop))
    X_train, X_test, Y_train, Y_test = X[:split], X[split:], Y[:split], Y[split:]

    culture_model_bad = LogisticRegression()
    culture_model_bad = culture_model_bad.fit(X_train, Y_train)

    result_culture_bad = culture_model_bad.predict_proba(X_test)
    result_culture_bad = pd.DataFrame(result_culture_bad)

    return dict(
        animals=animals_model_bad,
        culture=culture_model_bad,
        charity=charity_model_bad,
        education=education_model_bad,
        healthy=healthy_model_bad
    )


df_set = load_mashine()


p = {
    "first_name": "Фатима",
    "last_name": "Голоева",
    "sex": 1,
    "has_photo": 1,
    "has_mobile": 1,
    "home_phone": "",
    "site": "",
    "status": "жизнь прекрасна.",
    "verified": 0,
    "followers_count": 0,
    "occupation": "",
    "counters": "",
    "career": [],
    "contacts": "",
    "country": "",
    "games": ""
}


import vk
import json
from collections import OrderedDict
from config.settings import VK_TOKEN
from itertools import islice


user_vector = {}


def predict_animals(model, user_vector):
    pass


def predict_culture(model, user_vector):
    pass


def predict_charity(model, user_vector):
    pass


def predict_healthy(model, user_vector):
    pass


def predict_education(model, user_vector):
    pass


FIELDS = [
    'first_name',
    'last_name',
    'sex',
    'has_photo',
    'has_mobile',
    'home_phone',
    'site',
    'status',
    'verified',
    'followers_count',
    'occupation',
    'counters',
    'career',
    'contacts',
    'country',
    'games',
]


def ml_vk_processing(vk_id):
    vk_api = get_api()
    data = get_users_data(vk_api, str(vk_id), fields=FIELDS)


def get_api():
    session = vk.Session(access_token=VK_TOKEN)
    return vk.API(session, v='5.73', lang='ru', timeout=30)


def get_user_ids(vk_api, group_id):
    return vk_api.groups.getMembers(group_id=group_id, sort='id_desc', count=200)['items']


def get_users_data(vk_api, user_ids, fields):
    return vk_api.users.get(user_ids=user_ids, fields=fields)


