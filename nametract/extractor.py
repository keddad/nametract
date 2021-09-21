from typing import List
from nametract.tokenizer import *


def extract(inp: str) -> List[str]:
    """
    Extract anything that might be a name from text. Ignores things in the start of the sentence.
    :param inp: Text string to extract names from
    :return: List of strings with possible names
    """
    tokens = tokenize(inp)

    answ = []

    for t in tokens:
        if t.token_type == TokenEnum.Literal and t.contents[0].isupper():
            answ.append(t.contents)

    return answ
