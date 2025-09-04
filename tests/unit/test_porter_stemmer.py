from porter_stemmer import PorterStemmer


def test_stem(stemmer: PorterStemmer) -> None:
    assert stemmer.stem('взвесив') == 'взвес'
    assert stemmer.stem('программирование') == 'программирован'
    assert stemmer.stem('работающий') == 'работа'
    assert stemmer.stem('являться') == 'явля'
    assert stemmer.stem('стоит') == 'сто'
    assert stemmer.stem('полностью') == 'полност'
    assert stemmer.stem('радио') == 'рад'
