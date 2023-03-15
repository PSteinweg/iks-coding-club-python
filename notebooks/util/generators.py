import os
from datetime import datetime, timedelta
from humanize.time import precisedelta
import glob
from typing import Tuple


max = []



def files_with_dates(file_glob="./*") -> Tuple[str,datetime]:
    """ Iterates over a given file_glob and returns tuples of (file_path, modification_time).

    Args:
        file_glob (str, optional): Start directory given as a file glob. Defaults to "./*".

    Returns:
        Tuple[str,datetime]: Tuple (file_path, modification)

    Yields:
        Iterator[Tuple[str,datetime]]: _description_
    """
    
    for file in glob.glob(file_glob):
        modification_date = datetime.fromtimestamp(os.path.getmtime(file))
        absolute_file_path = os.path.abspath(file)
        if os.path.isfile(file):
            yield (absolute_file_path, modification_date)


