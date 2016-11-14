#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'bac'
from . import Request
import time
import hashlib
import struct


class ConnectReq(Request):
    def __init__(self, sp_id, sp_secret):
        _sp_id = sp_id.encode('utf-8')
        _sp_secret = sp_secret.encode("utf-8")
        _version = struct.pack('!B', 0x30)
        _timestamp = _get_strtime().encode('utf-8')
        _md5 = hashlib.md5(_sp_id + 9 * b'\0x00' + _sp_secret).digest()
        message_body = _sp_id + _md5 + _version + _timestamp
        Request.__init__(self, 0x00000001, message_body)


def _get_strtime():
    return time.strftime('%m%d%H%M%S', time.localtime(time.time()))
