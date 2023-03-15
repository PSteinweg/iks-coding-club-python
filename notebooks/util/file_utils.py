from datetime import datetime, timedelta
from humanize.time import precisedelta
from util.generators import *


def humanized_difference_between_dates(first_datetime: datetime, second_datetime: datetime) -> str:
    """
    The function returns the time difference between `first_datetime` and `second_datetime` in humanized form.

    Examples:
        date_1 = datetime.fromisoformat("2023-03-15T13:32:06+0000")
        date_2 = datetime.fromisoformat("2023-03-17T13:34:06+0000")
        humanized_difference_between_dates(date_1, date_2)
        -> '2 minutes and 2 seconds'

    Args:
        date_1 (datetime): first datetime
        date_2 (datetime): second datetime

    Returns:
        str: The difference between `first_datetime` and `second_datetime` in humanized form.
    """
    raise NotImplementedError


def find_old_files(file_glob: str ="./*",max_timedelta: timedelta=timedelta(days=30)):
    """ Prints all files that were modified before now - max_timedelta.

    Args:
        file_glob (str, optional): _description_. Defaults to "./*".
        max_timedelta (timedelta, optional): _description_. Defaults to timedelta(days=30).
    """
    for filename, modification_date in files_with_dates(file_glob):
        print(filename, modification_date)