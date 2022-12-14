import requests
from os.path import exists
import numpy


def divide_safely_with_0(a, b):
    a = a.astype(float)
    b = b.astype(float)
    return numpy.divide(
        a,
        b,
        out=numpy.zeros_like(a),
        where=b != 0
    ).astype(int)


def get_session_id(filename):
    with open(filename) as f:
        return f.read().strip()


def get_url(year, day):
    return f"https://adventofcode.com/{year}/day/{day}/input"


YEAR = 2022
SESSION_ID_FILE = "session.cookie"
SESSION = get_session_id(SESSION_ID_FILE)
HEADERS = {
    "User-Agent": "github.com/tomfran/advent-of-code-setup reddit:u/fran-sch, discord:@tomfran#5786"
}
COOKIES = {"session": SESSION}


def get_input(day):
    path = f"inputs/{day:02d}"

    if not exists(path):
        url = get_url(YEAR, day)
        response = requests.get(url, headers=HEADERS, cookies=COOKIES)
        if not response.ok:
            raise RuntimeError(
                f"Request failed\n\tstatus code: {response.status_code}\n\tmessage: {response.content}"
            )
        with open(path, "w") as f:
            f.write(response.text[:-1])

    with open(path, "r") as f:
        return f.read()


def get_test_input(day):
    path = f"aoc_2022_python/test_inputs/{day:02d}"
    with open(path, "r") as f:
        return f.read()


def sliding_window(list, length):
    for i in range(0, len(list) - length+1):
        yield list[i:i + length]
