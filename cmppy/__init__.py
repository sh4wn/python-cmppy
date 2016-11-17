#!/usr/bin/env python
# -*- coding: utf-8 -*-


from request import Request, ConnectReq, TerminateReq, SubmitReq
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

        if self._commence():
            self._write(request.message)
            response_message = self._read()
            res = parse_response(response_message)

            self._terminate()

            return res
        else:
            self._close()

        return None

    def _commence(self):
        """
        建立通道
        :return:
        """
        self._connect()
        connect_req = ConnectReq(self._sp_id, self._sp_secret)
        self._write(connect_req.message)
        response_message = self._read()
        if response_message:
            connect_res = parse_response(response_message)

            # TODO 验证网关响应的校验码
            # if connect_res.status == 0 and self._valid_auth(connect_req.authenticator_source, connect_res.raw_status,
            #                                                 connect_res.authenticator_ISMG):
            if connect_res.status == 0:
                return True

        return False

    def _terminate(self):
        """
        断开通道
        :return:
        """
        self._write(TerminateReq().message)
        response_message = self._read()
        if response_message:
            parse_response(response_message)
        self._close()

    def _connect(self):
        self._so.connect((self._host, self._port))

    def _write(self, message):
        print 'Write:' + message.encode('hex')
        self._so.send(message)

    def _read(self):
        content_length = self._so.recv(4)
        if content_length:
            length, = struct.unpack('!L', content_length)
            response = content_length + self._so.recv(length)
            print 'Read:' + response.encode('hex')
            return response
        return None

    def _close(self):
        self._so.close()

    def _valid_auth(self, authenticator_source, status, authenticator_ISMG):
        match_md5 = hashlib.md5(status + authenticator_source + self._sp_secret.encode("utf-8")).digest()
        print status.encode("hex") + ":" + authenticator_source.encode('hex')
        print match_md5.encode("hex") + ":" + authenticator_ISMG.encode("hex")
        return match_md5 == authenticator_ISMG
