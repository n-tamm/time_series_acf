"""
Utility helpers:
    check_dir: Creates directory if it does not exist
"""
from __future__ import annotations
from pathlib import Path

def check_dir(path: str) -> None:
    """
    :param path: Directory path
    :return: None
    """
    Path(path).mkdir(parents=True, exist_ok=True)
