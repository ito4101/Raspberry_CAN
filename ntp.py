#!/usr/bin/env python

import datetime
import ntplib
import sys
from time import ctime

try:
    version = 4
    client = ntplib.NTPClient()
    response = client.request(sys.argv[1], version)
    nowtime = datetime.datetime.strptime(ctime(response.tx_time), "%a %b %d %H:%M:%S %Y")
    print("Time       : " + nowtime.strftime('%Y/%m/%d %H:%M:%S'))
    print("Version    : " + str(response.version))
    print("Ref.ID     : " + ntplib.ref_id_to_text(response.ref_id))
    print("Offset     : " + str(response.offset))
    print("Leap       : " + ntplib.leap_to_text(response.leap))
    print("Root Delay : " + str(response.root_delay))
except Exception as e:
    print(e)
    sys.exit(1)