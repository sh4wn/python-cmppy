#!/usr/bin/env python
# -*- coding: utf-8 -*-

from . import Request
import struct

__author__ = 'bac'


class SubmitReq(Request):
    def __init__(self,
                 msg_src,
                 msg_content,
                 src_id='1064899103013',
                 dest_terminal_id=['8613900000000', ],
                 pk_total=1,
                 pk_number=1,
                 registered_delivery=0,
                 msg_level=0,
                 service_id='MI',
                 fee_usertype=2,
                 fee_terminal_id="",
                 fee_terminal_type=0,
                 tp_pid=0,
                 tp_udhi=0,
                 msg_fmt=8,
                 feetype='01',
                 feecode='000000',
                 valid_time=17 * '\x00',
                 at_time=17 * '\x00',
                 dest_terminal_type=0,
                 linkid=''):

        if len(msg_content) >= 70:
            raise ValueError("msg_content more than 70 words")
        if len(dest_terminal_id) > 100:
            raise ValueError("single submit more than 100 phone numbers")

        _msg_id = 8 * b'\x00'
        _pk_total = struct.pack('!B', pk_total)
        _pk_number = struct.pack('!B', pk_number)
        _registered_delivery = struct.pack('!B', registered_delivery)
        _msg_level = struct.pack('!B', msg_level)
        _service_id = (service_id + (10 - len(service_id)) * '\x00').encode('utf-8')
        _fee_usertype = struct.pack('!B', fee_usertype)
        _fee_terminal_id = (fee_terminal_id + (32 - len(fee_terminal_id)) * '\x00').encode('utf-8')
        _fee_terminal_type = struct.pack('!B', fee_terminal_type)
        _tp_pid = struct.pack('!B', tp_pid)
        _tp_udhi = struct.pack('!B', tp_udhi)
        _msg_fmt = struct.pack('!B', msg_fmt)
        _msg_src = msg_src.encode('utf-8')
        _feetype = feetype.encode('utf-8')
        _feecode = feecode.encode('utf-8')
        _valid_time = valid_time.encode('utf-8')
        _at_time = at_time.encode('utf-8')
        _src_id = (src_id + (21 - len(src_id)) * '\x00').encode('utf-8')
        _destusr_tl = struct.pack('!B', len(dest_terminal_id))
        _dest_terminal_id = b""
        for msisdn in dest_terminal_id:
            _dest_terminal_id += (msisdn + (32 - len(msisdn)) * '\x00').encode('utf-8')
        _dest_terminal_type = struct.pack('!B', dest_terminal_type)
        _msg_content = msg_content.encode('utf-16-be')
        _msg_length = struct.pack('!B', len(_msg_content))
        _linkid = (linkid + (20 - len(linkid)) * '\x00').encode('utf-8')
        _message_body = _msg_id + \
                        _pk_total + _pk_number + \
                        _registered_delivery + \
                        _msg_level + \
                        _service_id + \
                        _fee_usertype + _fee_terminal_id + \
                        _fee_terminal_type + \
                        _tp_pid + _tp_udhi + \
                        _msg_fmt + _msg_src + \
                        _feetype + _feecode + \
                        _valid_time + _at_time + \
                        _src_id + _destusr_tl + \
                        _dest_terminal_id + \
                        _dest_terminal_type + \
                        _msg_length + \
                        _msg_content + \
                        _linkid

        Request.__init__(self, 0x00000004, _message_body)
