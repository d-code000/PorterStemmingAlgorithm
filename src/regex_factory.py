class _RegexFactory:

    PERFECTIVE_GERUND_GROUP_1 = ['в', 'вши', 'вшись']
    PERFECTIVE_GERUND_GROUP_2 = ['ив', 'ивши', 'ившись', 'ыв', 'ывши', 'ывшись']

    ADJECTIVE = [
        'ее', 'ие', 'ые', 'ое', 'ими', 'ыми', 'ей', 'ий', 'ый', 'ой',
        'ем', 'им', 'ым', 'ом', 'его', 'ого', 'ему', 'ому', 'их', 'ых',
        'ую', 'юю', 'ая', 'яя', 'ою', 'ею'
    ]

    PARTICIPLE_GROUP_1 = ['ем', 'нн', 'вш', 'ющ', 'щ']
    PARTICIPLE_GROUP_2 = ['ивш', 'ывш', 'ующ']

    REFLEXIVE = ['ся', 'сь']

    VERB_GROUP_1 = [
        'ла', 'на', 'ете', 'йте', 'ли', 'й', 'л', 'ем', 'н', 'ло',
        'но', 'ет', 'ют', 'ны', 'ть', 'ешь', 'нно'
    ]
    VERB_GROUP_2 = [
        'ила', 'ыла', 'ена', 'ейте', 'уйте', 'ите', 'или', 'ыли', 'ей', 'уй',
        'ил', 'ыл', 'им', 'ым', 'ен', 'ило', 'ыло', 'ено', 'ят', 'ует',
        'уют', 'ит', 'ыт', 'ены', 'ить', 'ыть', 'ишь', 'ую', 'ю'
    ]

    NOUN = [
        'а', 'ев', 'ов', 'ие', 'ье', 'е', 'иями', 'ями', 'ами', 'еи',
        'ии', 'и', 'ией', 'ей', 'ой', 'ий', 'й', 'иям', 'ям', 'ием',
        'ем', 'ам', 'ом', 'о', 'у', 'ах', 'иях', 'ях', 'ы', 'ь',
        'ию', 'ью', 'ю', 'ия', 'ья', 'я'
    ]

    SUPERLATIVE = ['ейш', 'ейше']

    DERIVATIONAL = ['ост', 'ость']

    @staticmethod
    def __ending(func):
        def wrapper(*args, end=True, **kwargs):
            result = func(*args, **kwargs)
            return f'({result})$' if end else result
        return wrapper

    @staticmethod
    @__ending
    def get_perfective_gerund() -> str:
        return _RegexFactory.__assembling_groups(
            _RegexFactory.PERFECTIVE_GERUND_GROUP_1,
            _RegexFactory.PERFECTIVE_GERUND_GROUP_2,
        )

    @staticmethod
    @__ending
    def get_adjective() -> str:
        return _RegexFactory.__assembling_group(_RegexFactory.ADJECTIVE)

    @staticmethod
    def get_participle() -> str:
        return _RegexFactory.__assembling_groups(
            _RegexFactory.PARTICIPLE_GROUP_1,
            _RegexFactory.PARTICIPLE_GROUP_2,
        )

    @staticmethod
    @__ending
    def get_reflexive() -> str:
        return _RegexFactory.__assembling_group(_RegexFactory.REFLEXIVE)

    @staticmethod
    @__ending
    def get_verb() -> str:
        return _RegexFactory.__assembling_groups(
            _RegexFactory.VERB_GROUP_1,
            _RegexFactory.VERB_GROUP_2,
        )

    @staticmethod
    @__ending
    def get_noun() -> str:
        return _RegexFactory.__assembling_group(_RegexFactory.NOUN)

    @staticmethod
    @__ending
    def get_superlative() -> str:
        return _RegexFactory.__assembling_group(_RegexFactory.SUPERLATIVE)

    @staticmethod
    @__ending
    def get_derivational() -> str:
        return _RegexFactory.__assembling_group(_RegexFactory.DERIVATIONAL)

    @staticmethod
    @__ending
    def get_adjectival() -> str:
        """
        Целевая группа для удаления находится в match под индексом 1
        """
        return rf'\w+?(({_RegexFactory.get_participle()})?({_RegexFactory.get_adjective(end=False)}))'

    @staticmethod
    def __assembling_groups(group1: list[str], group2: list[str]) -> str:
        """
        Собирает группу для регулярного выражения, если группа состоит из 2х групп

        :param group1: Первая группа, которая должна начинаться с а или я
        :param group2: Вторая группа
        :return: Паттер для требуемой группы
        """
        return (rf'((?<=[ая])({_RegexFactory.__assembling_group(group1)}))'
                rf'|({_RegexFactory.__assembling_group(group2)})')

    @staticmethod
    def __assembling_group(ls: list) -> str:
        return r'|'.join(ls)
