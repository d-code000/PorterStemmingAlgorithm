import pytest

from porter_stemmer import PorterStemmer


@pytest.fixture(scope='session')
def stemmer() -> PorterStemmer:
    return PorterStemmer()


@pytest.fixture(scope='function')
def words() -> list[str]:
    with open('data/russian_words_10.txt', 'r', encoding='utf-8') as file:
        return file.read().split()
