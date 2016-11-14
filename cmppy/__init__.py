#!/usr/bin/env python
# -*- coding: utf-8 -*-


from request import Request
from response import parse_response
import socket
import struct

__author__ = 'bac'


class Cmppy:
    def __init__(self, host, port, sp_id, sp_secret):
        self._host = host
        self._port = port
        self._sp_id = sp_id
        self._sp_secret = sp_secret
        self._so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def request(self, request):
        self._write(request.message)
        response_message = self._read()
        connect_res = parse_response(response_message)

        if connect_res.status == 0x00:
            self._write(request.message)
            response_message = self._read()
            self._close()
            return parse_response(response_message)
        else:
            self._close()
            return None

    def _connect(self):
        self._so.connect((self._host, self._port))

    def _write(self, message):
        self._connect()
        self._so.send(message)

    def _read(self):
        content_length = self._so.recv(4)
        response = content_length + self._so.recv(struct.unpack('!L', content_length))
        return response

    def _close(self):
        self._so.close()
