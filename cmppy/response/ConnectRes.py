#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'bac'

from . import Response

import struct


class ConnectRes(Response):
    def __init__(self, message):
        Response.__init__(self, message)
        self.status = struct.unpack('!L', message[0:4])
        self.authenticator_ISMG = message[4:20].decode('utf-8')
        self.version = struct.unpack('!B', message[20:21])
