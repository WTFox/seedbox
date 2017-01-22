import time


def is_dir(file):
    """Takes <file> object and returns true if it's a directory."""
    return 'd' in file.longname[:3]


def convert_time(t):
    """Takes epoch time and translates it to a human readable version"""
    return time.strftime('%Y-%m-%d', time.localtime(t))