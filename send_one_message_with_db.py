#!/usr/bin/env python
# coding=utf-8
import can
import cantools
import time
from pprint import pprint
# db = cantools.database.load_file('dbc/motohawk.dbc')
# db = cantools.database.load_file('dbc/HU_S302-ICA_CAN_Matrix_V2.22_20200421.dbc')
db = cantools.database.load_file(   filename='dbc/motohawk.dbc',
                                    database_format=None,
                                    encoding="UTF-8",
                                    # encoding="GB2312",
                                    # encoding="GB18030",
                                    frame_id_mask=None,
                                    strict=False,
                                    cache_dir=None)

example_message1 = db.get_message_by_frame_id(496)
pprint(example_message1)
pprint(example_message1.signals)
msgdata1 = example_message1.encode({
'Temperature' : 0,
'AverageRadius' : 0,
'Enable' : 0},scaling=False,padding=False,strict=False)
msg1 = can.Message( arbitration_id=496, data=msgdata1, is_extended_id=False)

example_message2 = db.get_message_by_name('ExampleMessage')
msgdata2 = example_message2.encode({
'Temperature' : 1,  
'AverageRadius' : 1,
'Enable' : 1},scaling=False,padding=False,strict=False)
msg2 = can.Message( arbitration_id=0x1EA, data=msgdata2, is_extended_id=False)
with can.interface.Bus(bustype='canalystii', channel=0, baud=500000) as bus:
    try:
        bus.send(msg1)
        time.sleep(3)
        bus.send(msg2)
        print("Message sent on {bus.channel_info}")
    except can.CanError:
        print("Message NOT send")
