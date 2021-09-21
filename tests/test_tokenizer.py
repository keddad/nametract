from nametract.tokenizer import *
import pytest

testdata = [
    ("Привет, Мир!", [Token("Привет", token_type=TokenEnum.Literal), Token(",", token_type=TokenEnum.Punctuation),
                      Token("Мир", token_type=TokenEnum.Literal), Token("!", token_type=TokenEnum.Punctuation)])
]


class TestTokenizer:
    def test_simple(self):
        result_tokens = tokenize("Hello, my name is Pavel.")
        expected_tokens = [
            Token("Hello", token_type=TokenEnum.Literal),
            Token(",", token_type=TokenEnum.Punctuation),
            Token("my", token_type=TokenEnum.Literal),
            Token("name", token_type=TokenEnum.Literal),
            Token("is", token_type=TokenEnum.Literal),
            Token("Pavel", token_type=TokenEnum.Literal),
            Token(".", token_type=TokenEnum.Punctuation)
        ]

        assert result_tokens == expected_tokens

    def test_numbers(self):
        result_tokens = tokenize("The answer is 42!")
        expected_tokens = [
            Token("The", token_type=TokenEnum.Literal),
            Token("answer", token_type=TokenEnum.Literal),
            Token("is", token_type=TokenEnum.Literal),
            Token("42", token_type=TokenEnum.Number),
            Token("!", token_type=TokenEnum.Punctuation)
        ]

        assert result_tokens == expected_tokens

    @pytest.mark.parametrize("inp,exp", testdata)
    def test_different(self, inp, exp):
        assert tokenize(inp) == exp
