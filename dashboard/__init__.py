# dashboard/__init__.py

from .layouts import layout
from . import callbacks  # this just loads callbacks, even if not used directly

__all__ = ['layout']
