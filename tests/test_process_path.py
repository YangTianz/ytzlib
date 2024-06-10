from ytzlib.path_helper import search_by_exts, search_by_regex


def test_search_by_exts_py():
    ret = search_by_exts(
        ["tests/test_directory_tree"],
        ["py"],
    )
    assert len(ret) == 4


def test_search_by_exts_txt():
    ret = search_by_exts(
        ["tests/test_directory_tree"],
        ["txt"],
    )
    assert len(ret) == 6


def test_search_by_exts_txt_and_py():
    ret = search_by_exts(
        ["tests/test_directory_tree"],
        ["txt", "py"],
    )
    assert len(ret) == 10


def test_search_by_exts_md():
    ret = search_by_exts(
        ["tests/test_directory_tree"],
        ["md"],
    )
    assert len(ret) == 2


def test_search_by_exts_tx():
    ret = search_by_exts(
        ["tests/test_directory_tree"],
        ["tx"],
    )
    assert len(ret) == 0


def test_search_by_exts_pyc():
    ret = search_by_exts(
        ["tests/test_directory_tree"],
        ["tx"],
    )
    assert len(ret) == 0


def test_search_by_regex_1():
    ret = search_by_regex(
        ["tests/test_directory_tree"],
        ["[a-z]*"],
    )
    assert len(ret) == 12


def test_search_by_regex_1():
    ret = search_by_regex(
        ["tests/test_directory_tree"],
        ["[a-z]*[2]+"],
    )
    assert len(ret) == 5


def test_search_by_regex_2():
    ret = search_by_regex(
        ["tests/test_directory_tree"],
        ["[a-z]*[12]\.py"],
    )
    assert len(ret) == 2


def test_search_by_regex_2():
    ret = search_by_regex(
        ["tests/test_directory_tree"],
        ["[a-z]*[2]-[01]+\.py"],
    )
    assert len(ret) == 1
