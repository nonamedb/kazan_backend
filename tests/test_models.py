# coding: utf-8


import pytest
from backend import models


@pytest.mark.parametrize('model_class, fields', [
    ('Event', ['name', 'description', 'community_id', 'volunteer_count', 'bot', 'reward', 'event_subject_id']),
    ('EventSubject', ['name', ]),
])
def test_models_available(model_class, fields):
    model = getattr(models, model_class)
    for field in fields:
        assert hasattr(model, field)
