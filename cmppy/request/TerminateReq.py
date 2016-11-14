#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'bac'
from . import Request


class TerminateReq(Request):
    def __init__(self):
        message_body = b''
        Request.__init__(self, 0x00000002, message_body)
