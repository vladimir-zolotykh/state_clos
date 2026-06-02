#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
from abc import ABC, abstractmethod
from collections import OrderedDict


class Typed(ABC):
    def __init__(self, **kwds):
        for k, v in kwds:
            self.__dict__[k] = v

    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner=None):
        if instance is None:
            return self
        return instance.__dict__[self._name]

    @abstractmethod
    def validate(self, val):
        pass

    def __set__(self, instance, val):
        self.validate(val)
        instance.__dict__[self._name] = val


class String(Typed):
    def validate(self, val):
        if not isinstance(val, str):
            raise TypeError(f"{val} Expected str")


class Float(Typed):
    def validate(self, val):
        if not isinstance(val, float):
            raise TypeError(f"{val} Expected float")


class Integer(Typed):
    def validate(self, val):
        if not isinstance(val, int):
            raise TypeError(f"{val} Expected int")


class OrderedMeta(type):
    def __new__(mcls, clsname, bases, clsdict):
        fields: list[str] = []
        for key, val in clsdict.items():
            if isinstance(val, Typed):
                fields += key
                val.__set_name__(key)
        clsdict["_fields"] = fields
        return super().__new__(mcls, clsname, bases, clsdict)

    @classmethod
    def __prepare__(clsname, bases, **kwds):
        return OrderedDict()


class Person(Metaclass=OrderedMeta):
    name = String()
    weight = Float()
    reps = Integer()

    def __init__(self, name=name, weight=weight, reps=reps):
        self.name = name
        self.weight = weight
        self.reps = reps


if __name__ == "__main__":
    p = Person()
    print(p)
