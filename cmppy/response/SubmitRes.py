#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'bac'

from . import Response

import struct


class SubmitRes(Response):
    def __init__(self, message):
        Response.__init__(self, message)
        message_body = message[12:]
        self.msg_id, = struct.unpack('!Q', message_body[0:8])
        self.result, = struct.unpack('!L', message_body[8:12])
