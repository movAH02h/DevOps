from binary_search import search

array = [-100, -99, -1, 1, 2, 3, 4, 5, 6, 7, 8, 10, 33, 200]

targets = [2, 3, 5, 1, -100]

def test_first():
    assert search(array, 0, len(array) - 1, targets[0]) == targets[0]

def test_second():
    assert search(array, 0, len(array) - 1, targets[1]) == targets[1]

def test_third():
    assert search(array, 0, len(array) - 1, targets[2]) == targets[2]

def test_fourth():
    assert search(array, 0, len(array) - 1, targets[3]) == targets[3]

def test_fifth():
    assert search(array, 0, len(array) - 1, targets[4]) == targets[4]
