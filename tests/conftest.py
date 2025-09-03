import pytest

from porter_stemmer import PorterStemmer


@pytest.fixture(scope='session')
def stemmer() -> PorterStemmer:
    return PorterStemmer()
