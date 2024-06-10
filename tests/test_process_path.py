from ytzlib.path_helper import process_path


def test_process_path_py():
    ret = process_path(
        ["tests/test_directory_tree"],
        ["py"],
    )
    assert len(ret) == 4


def test_process_path_txt():
    ret = process_path(
        ["tests/test_directory_tree"],
        ["txt"],
    )
    assert len(ret) == 6


def test_process_path_txt_and_py():
    ret = process_path(
        ["tests/test_directory_tree"],
        ["txt", "py"],
    )
    assert len(ret) == 10


def test_process_path_md():
    ret = process_path(
        ["tests/test_directory_tree"],
        ["md"],
    )
    assert len(ret) == 2


def test_process_path_tx():
    ret = process_path(
        ["tests/test_directory_tree"],
        ["tx"],
    )
    assert len(ret) == 0


def test_process_path_pyc():
    ret = process_path(
        ["tests/test_directory_tree"],
        ["tx"],
    )
    assert len(ret) == 0
