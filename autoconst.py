#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
from typing import MutableMapping, Any
import re


class WilyDict(dict):
    def __init__(self, *args, **kwds):
        super().__init__(*args, **kwds)
        self.cnt = 0

    def __missing__(self, key):
        magic = re.compile(r"__\w+__")
        if magic.match(key):
            raise KeyError(key)
        n = self.cnt
        self.cnt += 1
        self[key] = n
        return n


class AutoMeta(type):
    @classmethod
    def __prepare__(
        metacls, name: str, bases: tuple[type, ...], /, **kwds: Any
    ) -> MutableMapping[str, object]:
        return WilyDict()


class Color(metaclass=AutoMeta):
    RED  # noqa: F821
    GREEN  # noqa: F821
    BLUE  # noqa: F821


if __name__ == "__main__":
    print(Color.RED, Color.GREEN, Color.BLUE)
