import re

import pytest

from regex_factory import RegexFactory


@pytest.fixture(scope='module')
def regex_factory():
    return RegexFactory()


def test_perfective_gerund(regex_factory: RegexFactory):
    pattern = regex_factory.get_perfective_gerund()

    # Группа 1
    assert re.search(pattern, 'сдав').group() == 'в'
    assert re.search(pattern, 'сдавши').group() == 'вши'

    # Группа 2
    assert re.search(pattern, 'встретив').group() == 'ив'
    assert re.search(pattern, 'встретивши').group() == 'ивши'


def test_adjective(regex_factory: RegexFactory):
    pattern = regex_factory.get_adjective()

    assert re.search(pattern, 'красивее').group() == 'ее'
    assert re.search(pattern, 'красивого').group() == 'ого'


def test_participle(regex_factory: RegexFactory):
    pattern = regex_factory.get_participle()

    # Группа 1
    assert re.search(pattern, 'причесанная').group() == 'нн'
    assert re.search(pattern, 'катаем').group() == 'ем'

    # Группа 2
    assert re.search(pattern, 'пингующий').group() == 'ующ'
    assert re.search(pattern, 'стримивший').group() == 'ивш'


def test_adjectival(regex_factory: RegexFactory):
    pattern = regex_factory.get_adjectival()

    # ADJECTIVE
    assert re.search(pattern, 'подареному').groups()[1] == 'ому'

    # PARTICIPLE + ADJECTIVE
    assert re.search(pattern, 'бегавшая').groups()[1] == 'вшая'

# Todo: дописать тесты для других групп окончаний
