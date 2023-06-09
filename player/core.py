"""Core Module"""


def load(filepath):
    """Loads data from filepath database"""
    try:
        with open(filepath) as file_:
            return(file_.read().strip().split("\n"))

    except FileNotFoundError as e:
        raise e
