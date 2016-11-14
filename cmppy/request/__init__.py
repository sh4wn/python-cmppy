#!/usr/bin/env python
# -*- coding: utf-8 -*-


import struct

_global_seq_no = 1


class Request:
    def __init__(self, command_id, message_body):
        self.command_id = command_id
        self._message_body = message_body

        global _global_seq_no
        _global_seq_no += 1
        self.sequence = _global_seq_no

        self.message = struct.pack('!L', 12 + len(self._message_body)) \
                       + struct.pack('!L', self.command_id) \
                       + struct.pack('!L', self.sequence) \
                       + self._message_body


from ConnectReq import ConnectReq
from TerminateReq import TerminateReq
