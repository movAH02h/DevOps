from search.binary_search import bin_search, array
import pytest

@pytest.mark.parametrize("array, target, result", [(array, 1, 1),
                                          (array, -100, -100),
                                          (array, 1000, -1),
                                          (array, 2, 2),
                                          (array, 4, -1)])
def test_binary_search(array, target, result):
    assert bin_search(array, 0, len(array) - 1, target) == result



