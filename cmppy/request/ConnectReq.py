#!/usr/bin/env python
# -*- coding: utf-8 -*-

from . import Request
import time
import hashlib
import struct

__author__ = 'bac'


class ConnectReq(Request):
    def __init__(self, sp_id, sp_secret):
        _sp_id = sp_id.encode('utf-8')
        _sp_secret = sp_secret.encode("utf-8")
        _version = struct.pack('!B', 0x30)
        _time_str = _get_strtime()
        _timestamp = struct.pack('!L', int(_time_str))
        self.authenticator_source = hashlib.md5(_sp_id + 9 * b'\x00' + _sp_secret + _time_str.encode('utf-8')).digest()
        message_body = _sp_id + self.authenticator_source + _version + _timestamp
        Request.__init__(self, 0x00000001, message_body)


def _get_strtime():
    return time.strftime('%m%d%H%M%S', time.localtime(time.time()))
