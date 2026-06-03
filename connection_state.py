#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
from multipledispatch import dispatch


class Connection:
    pass


class ConnectionState:
    def __repr__(self):
        return self.__class__.__name__


class OpenState(ConnectionState):
    pass


class ClosedState(ConnectionState):
    pass


@dispatch(Connection, ClosedState)
def write(conn, state):
    raise RuntimeError(f"{state}: cannot write")


@dispatch(Connection, OpenState)
def read(conn, state):
    print(f"{state}: reading")


@dispatch(Connection, ConnectionState)
def write(conn, state):  # noqa: F811
    print(f"{state}:  writing")


@dispatch(Connection, ClosedState)
def close(conn, state):  # noqa: F811
    raise RuntimeError(f"{state}: cannot close")


@dispatch(Connection, OpenState)
def close(conn, state):  # noqa: F811
    print(f"{state}: closing")


@dispatch(Connection, ClosedState)
def open(conn, state):
    print(f"{state}: opening")


@dispatch(Connection, OpenState)
def open(conn, state):  # noqa: F811
    raise RuntimeError(f"{state}: cannot open")


if __name__ == "__main__":
    conn = Connection()
    state = ClosedState()
    try:
        write(conn, state)
    except RuntimeError as exc:
        print(f"*** {exc}")
    open(conn, state)
    state = OpenState()
    try:
        open(conn, state)
    except RuntimeError as exc:
        print(f"*** {exc}")

    write(conn, state)
    read(conn, state)
    close(conn, state)
    state = ClosedState()
    try:
        close(conn, state)
    except RuntimeError as exc:
        print(f"*** {exc}")
