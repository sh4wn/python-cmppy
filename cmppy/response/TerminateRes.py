#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'bac'

from . import Response


class TerminateRes(Response):
    def __init__(self, message):
        Response.__init__(self, message)
