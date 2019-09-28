# coding: utf-8


import vk
import json
from collections import OrderedDict
from config.settings import VK_TOKEN
from itertools import islice


def chunk(it, size):
    it = iter(it)
    return iter(lambda: tuple(islice(it, size)), ())


subject_groups = {
    'charity': [
        'charity',
        'podaryzhizn',
    ],
    'animals': [
        'cat.gifs',
        '73749919',
    ],
    'education': [
        'v5inf',
        'skillbox_education'
    ],
    'healthy': [
        '109814200',
        'life.move',
    ],
    'culture': [
        'hermitage_museum',
        'tretyakovgallery',
    ]

}


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


def save_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f)


def load_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)


def get_api():
    session = vk.Session(access_token=VK_TOKEN)
    return vk.API(session, v='5.73', lang='ru', timeout=30)


def get_user_ids(api, group_id):
    return api.groups.getMembers(group_id=group_id, sort='id_desc', count=200)['items']


def get_users_data(api, user_ids, fields):
    return api.users.get(user_ids=user_ids, fields=fields)


def subject_groups_users_ids(api):
    res = {}
    for sg, group_ids in subject_groups.items():
        res[sg] = []
        for group in group_ids:
            res[sg].extend(get_user_ids(api, group))
    save_json(res, 'sg_user_ids.json')


def subject_groups_users_content():
    sg_user_ids = load_json('sg_user_ids.json')
    api = get_api()

    for subject, items in sg_user_ids.items():
        with open(f'{subject}.json', 'w') as f:
            res = []
            for ch in chunk(items, 100):
                res.extend([{field: user.get(field, '') for field in FIELDS} for user in get_users_data(api, user_ids=','.join([str(c) for c in ch]), fields=FIELDS)])
            json.dump(res, f, ensure_ascii=True)
