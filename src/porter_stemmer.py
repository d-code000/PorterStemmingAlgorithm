import re

from regex_factory import RegexFactory


class PorterStemmer:

    @staticmethod
    def stem(word: str) -> str:
        pass

    @staticmethod
    def __step1(word: str) -> str:
        """
        В последовательном порядке пытаемся удалить все виды окончаний.
        """
        patterns = [
            RegexFactory.get_perfective_gerund(),
            RegexFactory.get_reflexive(),
            RegexFactory.get_adjectival(),
            RegexFactory.get_verb(),
            RegexFactory.get_noun()
        ]

        for pattern in patterns:
            cut = re.sub(pattern, '', word)
            if cut != word:
                return cut

        return word

    @staticmethod
    def __step2(word: str) -> str:
        pass

    @staticmethod
    def __step3(word: str) -> str:
        pass

    @staticmethod
    def __step4(word: str) -> str:
        pass
