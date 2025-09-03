import re

from regex_factory import RegexFactory


class PorterStemmer:
    """
    Step 1-4 возвращают количество символов, которые должны быть удалены с конца строки
    """
    VOWELS = 'аеиоуыэюя'

    @staticmethod
    def stem(word: str) -> str:
        word = PorterStemmer.__step0(word)

        rv_index = PorterStemmer.__get_rv_index(word)
        if rv_index is None: return word

        remove_len = 0
        remove_len += PorterStemmer.__step1(word[rv_index:len(word) - remove_len])
        remove_len += PorterStemmer.__step2(word[rv_index:len(word) - remove_len])

        return word[:len(word) - remove_len]

    @staticmethod
    def __step0(word: str) -> str:
        return word.lower().replace('ё', 'е')

    @staticmethod
    def __step1(word: str) -> int:
        patterns = [
            RegexFactory.get_perfective_gerund(),
            RegexFactory.get_reflexive(),
            RegexFactory.get_verb(),
            RegexFactory.get_noun()
        ]

        for pattern in patterns:
            match = re.search(pattern, word)
            if match: return len(match.group(0))

        match = re.search(RegexFactory.get_adjectival(), word)
        if match: return len(match.group(1))

        return 0

    @staticmethod
    def __step2(word: str) -> int:
        match = re.search(r'\b(\w+)и\b', word)
        if match: return len(match.group(0))
        return 0

    @staticmethod
    def __step3(word: str) -> str:
        pass

    @staticmethod
    def __step4(word: str) -> str:
        pass

    @staticmethod
    def __get_rv_index(word: str) -> int | None:
        """
        :return: Начальный индекс области rv (None, если область пуста)
        :returns
        """
        for i in range(len(word) - 1):  # Проверяем до предпоследней буквы
            if word[i] in PorterStemmer.VOWELS:
                return i + 1  # Возвращаем индекс следующей буквы за гласной
        return None

    @staticmethod
    def __get_r1_index(word: str) -> int | None:
        """
        :return: Начальный индекс области r1 (None, если область пуста)
        """
        last_is_vowel = False
        for i in range(len(word) - 1):  # Проверяем до предпоследней буквы
            if word[i] in PorterStemmer.VOWELS:
                last_is_vowel = True
                continue
            if word[i] not in PorterStemmer.VOWELS and last_is_vowel:
                return i + 1
            last_is_vowel = False
        return None

    @staticmethod
    def __get_r2_index(word: str) -> int | None:
        """
        :return: Начальный индекс области r2 (None, если область пуста)
        """
        r1_index = PorterStemmer.__get_r1_index(word)
        if r1_index is None: return None
        return PorterStemmer.__get_r1_index(word[r1_index:])
