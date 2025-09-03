import pytest

from porter_stemmer import PorterStemmer


@pytest.fixture(scope='module')
def stemmer() -> PorterStemmer:
    return PorterStemmer()


def test_stem(stemmer: PorterStemmer) -> None:
    assert stemmer.stem('взвесив') == 'взвес'
