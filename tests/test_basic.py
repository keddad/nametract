from nametract import extract
import pytest

testdata = [
    ("Привет, Ваня!", ["Ваня"]),
    ("Hello, Ivan!", ["Ivan"]),
    ("Он убил Андрея и Марию", ["Андрея", "Марию"]),
    ("К нему подошел Иван Иванович Барашкин", ["Иван Иванович Барашкин"]),
    ("К нему подошел Иван, Иванович Барашкин", ["Иван", "Иванович Барашкин"]),
    ("С коня сошел Иван Зайцев-Кабачков", ["Иван Зайцев-Кабачков"]),
    ("Алексей Петрович был убит", ["Алексей Петрович"]),
    ("Правительство было создано. Канцлер был убит.", []),
    ("\"Создание рабочих мест важно. Также важен Владимир Путин.\"", ["Владимир Путин"])
]


class TestBasic:
    @pytest.mark.parametrize("inp,expected", testdata)
    def test_simple_names(self, inp, expected):
        assert extract(inp) == expected

    def test_name_size(self):
        extracted = extract("Там стоял Инь Сунь и Андрей", minimal_name_size=4)
        assert extracted == ["Сунь", "Андрей"]

    def test_ignore_sentence_start(self):
        extracted = extract("Андрей и Петр подошли к столу.", ignore_sentence_start=False)
        assert extracted == ["Андрей", "Петр"]
