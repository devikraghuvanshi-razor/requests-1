"""Sink e2e test file; safe to delete."""


def average(values):
    # Bug on purpose: divides by zero for an empty list.
    return sum(values) / len(values)


def read_config(path):
    # Bug on purpose: the file is never closed.
    handle = open(path)
    return handle.read()
