#!/usr/bin/python
# -*- coding: utf-8 -*-
import datetime
from datetime import timedelta
import os
import time

import pytz
from dotenv import load_dotenv
load_dotenv(verbose=True)


#---------------------------#
# APPLICATION CONFIGURATION #
#---------------------------#

"""
Variables used for configuring the how the serial USB communication will be
handled with the Arduino device.
"""
SERIAL_PORT = os.getenv("SERIAL_PORT")
SERIAL_BAUD = int(os.getenv("SERIAL_BAUD"))
SERIAL_TIMEOUT = int(os.getenv("SERIAL_TIMEOUT"))


"""
Variable controls what timezone formatting we must apply to our UTC datetimes.
"""
LOCAL_TIMEZONE = pytz.timezone(os.getenv("LOCAL_TIMEZONE_NAME"))


#------------------#
# GLOBAL CONSTANTS #
#------------------#

"""
Simple variable used to send to the Arduino device.
"""
RX_BYTE = '1'.encode('UTF-8')


"""
The following variables are unique identifiers for the available commands in
our service to the users.
"""
SET_WIFI_COMMAND_ID = 1


#-------------------#
# UTILITY FUNCTIONS #
#-------------------#

def getDT():
    """
    Function will return the current datetime aware of the local timezone.
    """
    # Get our UTC datetime without any timezone awareness.
    naive_now_dt = datetime.datetime.utcnow()

    # Convert to our local timezone.
    utc_aware_now_dt = naive_now_dt.replace(tzinfo=pytz.utc) # Make UTC timezone aware.
    local_aware_now_dt = utc_aware_now_dt.astimezone(LOCAL_TIMEZONE) # Convert to local timezone.

    # Return our datetime converted to our local timezone.
    return local_aware_now_dt
