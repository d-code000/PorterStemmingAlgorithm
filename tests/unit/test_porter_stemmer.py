import pytest

from porter_stemmer import PorterStemmer


@pytest.fixture(scope='module')
def stemmer():
    return PorterStemmer()


def test_stem(stemmer: PorterStemmer):
    assert stemmer.stem('взвесив') == 'взвес'
