
import utils.arrs


def test_get():
    assert utils.arrs.get([1, 2, 3], 1, "test") == 2
    assert utils.arrs.get([], 0, "test") == "test"


def test_slice():
    assert utils.arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert utils.arrs.my_slice([1, 2, 3], 1) == [2, 3]
