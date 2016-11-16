#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'bac'

import struct


class Response:
    def __init__(self, message):
        self.length, = struct.unpack('!L', message[0:4])
        self.command_id, = struct.unpack('!L', message[4:8])
        self.sequence, = struct.unpack('!L', message[8:12])
        self.message_body = message[12:self.length]


from ConnectRes import ConnectRes
from TerminateRes import TerminateRes

_res_mapping = {0x80000001: ConnectRes
    , 0x80000002: TerminateRes}


def parse_response(message):
    print message.encode('hex')
    command_id, = struct.unpack('!L', message[4:8])
    return _res_mapping[command_id](message)
