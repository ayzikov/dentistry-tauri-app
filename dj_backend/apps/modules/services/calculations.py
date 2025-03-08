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
    :param teeth: словарь с номерами зубов и их баллами {"t_11": 2}
    :return: индекс
    """
    return round(len(teeth), 1)

