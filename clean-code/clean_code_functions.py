#  @uthor: Dr.-Ing. Joan MOUBA, joan.mouba@gmail.com

import csv
from pathlib import Path
from typing import Dict
from pprint import pprint

def load_data(csv_file_path: str) -> Dict:
    """ Returns data from a csv to a dictionary
    Args:
        csv_file_path (str): path to the file containing the data
    Returns:
        dict
     """
    path = Path(csv_file_path)

    with path.open(mode="r") as fd:
        file_read = csv.reader(fd)
        next(file_read)  # skip the header
        data = {
            row[0].strip(): row[1].strip()
            for row in file_read
        }  # dict comprehension
    return data


if __name__ == '__main__':
    extracted_data = load_data("./data.csv")
    pprint(extracted_data)
