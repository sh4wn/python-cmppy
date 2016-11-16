#!/usr/bin/env python
# -*- coding: utf-8 -*-

from . import Request

__author__ = 'bac'


class SubmitReq(Request):
    def __init__(self,
                 msg_src,
                 pk_total=1,
                 pk_number=1,
                 registered_delivery=0,
                 msg_level=1,
                 service_id='',
                 fee_usertype=2,
                 fee_terminal_id=0,
                 fee_terminal_type=0,
                 tp_pid=0,
                 tp_udhi=0,
                 msg_fmt=0,
                 fee_type='02',
                 fee_code='000000',
                 valid_time=17 * b'\0x00'
                 ):
        pass
