import datetime
""" Различные функции """


def get_greetings(time_now=None) -> str:
    """ Возвращает приветствие в зависимости от времени суток """
    time_now = datetime.datetime.now() if time_now is None else time_now
    if time_now.hour in range(4, 16): return "добрый день"
    else: return "добрый вечер"


def to_fixed(numObj, digits=2) -> str:
    """ Возвращает любое число с плавающей запятой в красивом виде """
    return f"{numObj:.{digits}f}"
