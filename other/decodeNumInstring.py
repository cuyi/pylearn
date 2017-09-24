#! /usr/bin/env python
fields = ['\x05ItemId', '\x1bSystime', '\x10CRNTI', '\x10LTETime']

for field in fields:
    print int(field[0].encode('hex'), 16),
    print field[1:]



