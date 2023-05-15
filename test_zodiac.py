from zodiac import check_format, get_zodiac, generate_sign, read_csv
import pytest


def main():
    test_check_format()
    test_get_zodiac()
    test_generate_sign()


@pytest.fixture
def list():
    list = read_csv("./horoscopes.csv")
    return list


def test_check_format():
    assert check_format("3/20") == (3, 20)
    assert check_format("05/15") == (5, 15)
    assert check_format("26/05") == False


def test_get_zodiac():
    assert get_zodiac(4, 21) == "Taurus"
    assert get_zodiac(10, 20) == "Libra"
    assert get_zodiac(5, 25) == "Gemini"


def test_generate_sign(list):
    assert generate_sign("Leo", list) == "♌︎"
    assert generate_sign("Scorpio", list) == "♏︎"
    assert generate_sign("Pisces", list) == "♓︎"


if __name__ == "__main__":
    main()