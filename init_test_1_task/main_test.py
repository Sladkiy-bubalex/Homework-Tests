import pytest
import function


# Тесты для функий из первой задачи
def test_add_function_success():
    type_ = "snils"
    number = "5624 894216"
    name = "Ололош Ололоев"
    directoria = 2
    result_documents, result_directories_2 = function.add(
        type_, number, name, directoria
    )
    assert len(result_documents) == 5
    assert len(result_directories_2["2"]) == 3


@pytest.mark.xfail
@pytest.mark.parametrize(
    "type_,number,name,directoria", [("snils", "5624 894216", "Ололош Ололоев", 2)]
)
def test_add_function_failed(type_, number, name, directoria):
    result_documents, result_directories_2 = function.add(
        type_, number, name, directoria
    )
    assert len(result_documents) == 4


def test_get_name_sucsess():
    result = function.get_name("5624 894216")
    assert result == "Ололош Ололоев"


@pytest.mark.parametrize("number", [("1231231")])
def test_get_name_failed(number):
    result = function.get_name(number)
    assert result == "Документ не найден"


@pytest.mark.parametrize("number_doc", [("5624 894216")])
def test_get_directory_sucsess(number_doc):
    result = function.get_directory(number_doc)
    assert result == "2"


def test_get_directory_failed():
    result = function.get_directory("How do you do")
    assert result == "Полки с таким документом не найдено"


# Тесты для функий из второй задачи
@pytest.mark.parametrize("a, b, c, expected", [(3, 8, 15, -116), (8, 31, 4, 833)])
def test_discriminant_sucsess(a, b, c, expected):
    result = function.discriminant(a, b, c)
    assert result == expected


@pytest.mark.xfail
def test_discriminant_failed():
    try:
        result = function.discriminant(5, "4", "Volodya")
    except TypeError as error:
        assert result == error


@pytest.mark.parametrize(
    "a, b, c, expected",
    [
        (481, 3, 0, (0.0, -0.006237006237006237)),
        (23, 442, 31, (-0.07039359944202586, -19.1469977049058)),
    ],
)
def test_solution_sucsess_roots_of_the_equation(a, b, c, expected):
    result = function.solution(a, b, c)
    assert result == expected


def test_solution_sucsess_with_zero_roots():
    result = function.solution(-4, 28, -49)
    assert result == 3.5


def test_solution_sucsess_not_roots():
    result = function.solution(953, 0, 352)
    assert result == "корней нет"


@pytest.mark.xfail
def test_solution_failed():
    try:
        result = function.solution(3.5, False, "Hello")
    except TypeError as error:
        assert result == error


# Тесты для функий из третьей задачи
@pytest.mark.parametrize(
    "list_vote, expected", [([4, 7, 9, 11, 4, 7, 3], 4), ([5, 33, 3, 5, 87, 3], 5)]
)
def test_vote_sucsess(list_vote, expected):
    result = function.vote(list_vote)
    assert result == expected

