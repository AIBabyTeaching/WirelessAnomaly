"""Simple timing context manager."""
from __future__ import annotations
import time
from contextlib import contextmanager


@contextmanager
def timed() -> float:
    start = time.time()
    yield lambda: time.time() - start
