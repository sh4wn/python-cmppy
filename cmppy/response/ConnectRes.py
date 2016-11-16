#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'bac'

from . import Response

import struct


class ConnectRes(Response):
    def __init__(self, message):
        Response.__init__(self, message)
        message_body = message[12:]
        self.raw_status = message_body[0:4]
        self.status, = struct.unpack('!L', self.raw_status)
        self.authenticator_ISMG = message_body[4:20]
        self.version, = struct.unpack('!B', message_body[20:21])
