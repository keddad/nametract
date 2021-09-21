from typing import List
from enum import Enum
from dataclasses import dataclass


class TokenEnum(Enum):
    Literal = 1
    Number = 2
    Punctiation = 3


@dataclass
class Token:
    contents: str
    token_type: TokenEnum


def tokenize(inp: str) -> List[Token]:
    # TODO Proper tokenizing

    answ = []
    for word in inp.split():
        if word[0].isalpha():
            answ.append(Token(word, TokenEnum.Literal))
        else:
            answ.append(Token(word, TokenEnum.Number))

    return answ
