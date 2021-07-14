#!/usr/bin/env python
# coding=utf-8
import can
import time

# can.rc['interface'] = 'canalystii'
# can.rc['channel'] = '0'
# can.rc['bitrate'] = 500000

def send_one():
    msg1 = can.Message( arbitration_id=496, data=[255, 255,255,255,255,255,255,255], is_extended_id=False)
    msg2 = can.Message( arbitration_id=0x1EA, data=[  0,   0,  0,  0,  0,  0,  0,  0], is_extended_id=False)
    msg3 = can.Message( arbitration_id=0x1EA, data=[255, 255,255,255,255,255,255,255], is_extended_id=False)
    with can.interface.Bus(bustype='canalystii', channel=0, baud=500000) as bus:
        try:
            bus.send(msg1)
            time.sleep(3)
            bus.send(msg2)
            time.sleep(3)
            bus.send(msg3)
            print("Message sent on {bus.channel_info}")
        except can.CanError:
            print("Message NOT send")

if __name__ == "__main__":
    send_one()
