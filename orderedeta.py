#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
from typing import MutableMapping, Any
from collections import OrderedDict


# class Typed(ABC):
class Typed:
    def __init__(self, **kwds):
        for k, v in kwds.items():
            self.__dict__[k] = v

    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner=None):
        if instance is None:
            return self
        return instance.__dict__[self._name]

    def validate(self, val) -> None:
        if not isinstance(val, self._expected_type):
            raise TypeError(f"{val} Expected {self._expected_type}")

    def __set__(self, instance, val):
        self.validate(val)
        instance.__dict__[self._name] = val


class String(Typed):
    _expected_type = str


class Float(Typed):
    _expected_type = float


class Integer(Typed):
    _expected_type = int


class OrderedMeta(type):
    def __new__(mcls, clsname, bases, clsdict):
        fields: list[str] = []
        for key, val in clsdict.items():
            if isinstance(val, Typed):
                fields.append(key)
                val.__set_name__(None, key)
        clsdict["_fields"] = fields
        return super().__new__(mcls, clsname, bases, clsdict)

    @classmethod
    def __prepare__(
        metacls, name: str, bases: tuple[type, ...], /, **kwds: Any
    ) -> MutableMapping[str, object]:
        return OrderedDict()


class Exercise(metaclass=OrderedMeta):
    _fields: list[str] = []

    name = String()
    weight = Float()
    reps = Integer()

    def __init__(self, name=name, weight=weight, reps=reps):
        self.name = name
        self.weight = weight
        self.reps = reps


if __name__ == "__main__":
    p = Exercise(name="bench", weight=77.5, reps=2)
    print(p.__dict__, p._fields)
