from porter_stemmer import PorterStemmer


def test_stem(stemmer: PorterStemmer) -> None:
    # assert stemmer.stem('взвесив') == 'взвес'
    assert stemmer.stem('программирование') == 'программирован'
