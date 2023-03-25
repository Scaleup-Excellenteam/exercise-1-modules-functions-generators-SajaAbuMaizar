import os


def deep_files(path):
    files = os.listdir(path)
    deep_named_files = filter(lambda x: x.startswith('deep'), files)
    return list(deep_named_files)