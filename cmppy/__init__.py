#!/usr/bin/env python
# -*- coding: utf-8 -*-


from request import Request, ConnectReq
from response import parse_response
import socket
import struct
import hashlib

__author__ = 'bac'


class Cmppy:
    def __init__(self, host, port, sp_id, sp_secret):
        self._host = host
        self._port = port
        self._sp_id = sp_id
        self._sp_secret = sp_secret
        self._so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def request(self, request):

        connect_req = ConnectReq(self._sp_id, self._sp_secret)
        connect_req.authenticator_source
        self._write(connect_req.message)
        response_message = self._read()
        connect_res = parse_response(response_message)
        if connect_res.status != 0 or not self._valid_auth(connect_req.authenticator_source, connect_res.raw_status,
                                                           connect_res.authenticator_ISMG):
            return None

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
        print 'Write:' + message.encode('hex')
        self._connect()
        self._so.send(message)

    def _read(self):
        content_length = self._so.recv(4)
        length, = struct.unpack('!L', content_length)
        response = content_length + self._so.recv(length)
        return response

    def _close(self):
        self._so.close()

    def _valid_auth(self, authenticator_source, status, authenticator_ISMG):
        match_md5 = hashlib.md5(status + authenticator_source + self._sp_secret.encode("utf-8")).digest()
        print status.encode("hex")+":"+authenticator_source.encode('hex')
        print match_md5.encode("hex") + ":" + authenticator_ISMG.encode("hex")
        return match_md5 == authenticator_ISMG
