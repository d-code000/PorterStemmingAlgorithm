import re

from regex_factory import RegexFactory


class PorterStemmer:
    """
    Step 1-4 возвращают количество символов, которые должны быть удалены с конца строки
    """
    VOWELS = 'аеиоуыэюя'

    @staticmethod
    def stem(word: str) -> str:
        word = PorterStemmer.__normalize(word)

        rv_index = PorterStemmer.__get_rv_index(word)
        if rv_index is None: return word

        remove_len = 0
        remove_len += PorterStemmer.__step1(word[rv_index:len(word) - remove_len])
        remove_len += PorterStemmer.__step2(word[rv_index:len(word) - remove_len])

        r2_index = PorterStemmer.__get_r2_index(word)
        if r2_index:
            remove_len += PorterStemmer.__step3(word[r2_index:len(word) - remove_len])

        remove_len += PorterStemmer.__step4(word[rv_index:len(word) - remove_len])

        return word[:len(word) - remove_len]

    @staticmethod
    def __normalize(word: str) -> str:
        return word.lower().replace('ё', 'е')

    @staticmethod
    def __step1(area: str) -> int:
        patterns = [
            # Паттерн - целевая группа
            [RegexFactory.get_perfective_gerund(), 1],
            [RegexFactory.get_reflexive(), 1],
            [RegexFactory.get_adjectival(), 2],
            [RegexFactory.get_verb(), 1],
            [RegexFactory.get_noun(), 1]
        ]

        for pattern, target_group in patterns:
            match_len = PorterStemmer.__get_match_len(area, pattern, target_group)
            if match_len > 0: return match_len

        return 0

    @staticmethod
    def __step2(area: str) -> int:
        return PorterStemmer.__get_match_len(area, r'\b(\w+)и\b')

    @staticmethod
    def __step3(area: str) -> int:
        return PorterStemmer.__get_match_len(area, RegexFactory.get_derivational())

    @staticmethod
    def __step4(area: str) -> int:
        remove_len = 0
        match = re.search(RegexFactory.get_superlative(), area)
        if match: remove_len += len(match.group(0))
        new_area = area[:len(area) - remove_len]
        if len(new_area) >= 2 and new_area[-2:] == 'нн':
            remove_len += 1
        if len(new_area) >= 1 and new_area[-1] == 'ь':
            remove_len += 1
        return remove_len

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

    @staticmethod
    def __get_match_len(area: str, pattern: str, target_group=0) -> int:
        match = re.search(pattern, area)
        if match: return len(match.group(target_group))
        return 0
