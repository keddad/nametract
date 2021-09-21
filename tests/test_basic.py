from nametract import extract
import pytest

testdata = [
    ("Привет, Ваня!", ["Ваня"]),
    ("Hello, Ivan!", ["Ivan"]),
    ("Он убил Андрея и Марию", ["Андрея", "Марию"]),
    ("К нему подошел Иван Иванович Барашкин", ["Иван Иванович Барашкин"])
]


class TestBasic:
    @pytest.mark.parametrize("inp,expected", testdata)
    def test_simple_names(self, inp, expected):
        assert extract(inp) == expected
