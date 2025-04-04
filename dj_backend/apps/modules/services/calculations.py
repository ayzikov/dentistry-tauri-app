def ohis_calculate(teeth: dict) -> float:
    """
    Расчет индекса OHI-S
    :param teeth: словарь с номерами зубов и их баллами {"t_11": 2}
    :return: индекс
    """
    # суммируем баллы и делим на количество обследуемых зубов и округляем до 1 знака после запятой
    res = sum(teeth.values()) / len(teeth)
    return round(res, 1)


def pi_calculate(teeth: dict) -> float:
    """
    Расчет индекса ПИ
    :param teeth: словарь с номерами зубов и их баллами {"t_11": 2}
    :return: индекс
    """
    # суммируем баллы и делим на количество обследуемых зубов и округляем до 1 знака после запятой
    res = sum(teeth.values()) / len(teeth)
    return round(res, 1)


def pma_calculate(teeth: dict) -> float:
    """
    Расчет индекса PMA
    :param teeth: словарь с номерами зубов и их баллами {"t_11": 2}
    :return: индекс
    """
    res = (sum(teeth.values()) / (3 * len(teeth))) * 100
    return round(res, 1)


def cpitn_calculate(teeth: dict) -> float:
    """
    Расчет индекса CPITN
    :param teeth: словарь с номерами зубов и их баллами {"t_11": 2}
    :return: индекс
    """
    return max(teeth.values())


def cpu_calculate(teeth: dict) -> float:
    """
    Расчет индекса КПУ
    :param teeth: словарь с номерами зубов и их буквами {"t_11": ["П", "O"]}
    :return: индекс
    """

    # считаем количество зубов у которых одна из букв in check_list
    index_counter = 0
    check_list = ["С", "П", "О"]
    for tooth_letters in teeth.values():
        # проверяем чтобы хотя бы одна буква из tooth_letters была в check_list
        if any(map(lambda letter: letter in check_list, tooth_letters)):
            index_counter += 1

    return index_counter

