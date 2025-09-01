class RegexFactory:
    VOWELS = 'аеиоуыэюя'

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
    def get_perfective_groups() -> str:
        return RegexFactory.__assembling_groups(
            RegexFactory.PERFECTIVE_GERUND_GROUP_1,
            RegexFactory.PERFECTIVE_GERUND_GROUP_2,
        )

    @staticmethod
    def __assembling_groups(group1: list[str], group2: list[str]) -> str:
        """
        :param group1: Первая группа, которая должна начинаться с а или я
        :param group2: Вторая группа
        :return: Паттер для требуемой группы
        """
        return (f'(?<=[ая])({RegexFactory.__get_pattern_group(RegexFactory.PERFECTIVE_GERUND_GROUP_1)})$'
                f'|(?<=\w)({RegexFactory.__get_pattern_group(RegexFactory.PERFECTIVE_GERUND_GROUP_2)})$')

    @staticmethod
    def __get_pattern_group(ls: list) -> str:
        return '|'.join(ls)
