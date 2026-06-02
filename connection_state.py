#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
from multipledispatch import dispatch


class Connection:
    pass


class ConnectionState:
    pass


class OpenState(ConnectionState):
    pass


class ClosedState(ConnectionState):
    pass


@dispatch(Connection, ConnectionState)
def open(conn, state):
    pass


@dispatch(Connection, ConnectionState)
def close(conn, state):
    pass


@dispatch(Connection, OpenState)
def read(conn, state):
    print("reading")


@dispatch(Connection, OpenState)
def write(conn, state):
    print("writing")
