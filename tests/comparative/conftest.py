import pytest


@pytest.fixture(scope='function', params=['10', '2000'])
def words(request) -> list[str]:
    filename = f'data/russian-words-{request.param}.txt'
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read().split('\n')

