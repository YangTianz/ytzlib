import os
import re


def process_path(input_paths: list[str], exts: list[str]) -> list[str]:
    """处理输入路径"""
    ret = []
    for input_path in input_paths:
        if os.path.isdir(input_path):
            for path, _, file_names in os.walk(input_path):
                for file_name in file_names:
                    for ext in exts:
                        if file_name.endswith(ext):
                            ret.append(os.path.join(path, file_name))
        else:
            for ext in exts:
                if input_path.endswith(ext):
                    ret.append(input_path)
    return ret


def search_by_exts(input_paths: list[str], exts: list[str]) -> list[str]:
    ret = []
    for input_path in input_paths:
        if os.path.isdir(input_path):
            for path, _, file_names in os.walk(input_path):
                for file_name in file_names:
                    for ext in exts:
                        if file_name.endswith(ext):
                            ret.append(os.path.join(path, file_name))
        else:
            for ext in exts:
                if input_path.endswith(ext):
                    ret.append(input_path)
    return ret


def search_by_regex(
    input_paths: list[str], regex_patterns: list[str]
) -> list[str]:
    patterns = [re.compile(p) for p in regex_patterns]
    ret = []
    for input_path in input_paths:
        if os.path.isdir(input_path):
            for path, _, file_names in os.walk(input_path):
                for file_name in file_names:
                    for pattern in patterns:
                        if pattern.match(file_name) is not None:
                            ret.append(os.path.join(path, file_name))
        else:
            for pattern in patterns:
                if pattern.match(input_paths) is not None:
                    ret.append(input_path)
    return ret
