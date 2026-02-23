import pytest

#4.Mark a failing test as xfail with reason : "Bug #123"
@pytest.mark.xfail(reason="Bug #123")
def test_with_bug():
    assert 2 + 1 == 4

#5. 5 parametrized cases - 2 are known bugs - mark only 2 cases as xfail not entire

@pytest.mark.parametrize(
    "a,b,expected",
    [
        (2, 3, 5),
        (4, 5, 9),
        pytest.param(2, 2, 5, marks=pytest.mark.xfail(reason="Bug #123")),
        pytest.param(3, 3, 10, marks=pytest.mark.xfail(reason="Bug #124")),
        (10, 0, 10),
    ]
)
def test_add(a, b, expected):
    assert a + b == expected