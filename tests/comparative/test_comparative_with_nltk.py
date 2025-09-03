import pytest
from nltk import SnowballStemmer

from porter_stemmer import PorterStemmer


@pytest.fixture(scope='module')
def nltk_stemmer() -> SnowballStemmer:
    return SnowballStemmer('russian')


def test_comparate(stemmer: PorterStemmer, nltk_stemmer: SnowballStemmer, words: list[str]) -> None:
    for word in words:
        assert stemmer.stem(word) == nltk_stemmer.stem(word)
