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
Variable controls what timezone formatting we must apply to our UTC datetimes.
"""
LOCAL_TIMEZONE = pytz.timezone(os.getenv("LOCAL_TIMEZONE_NAME"))

"""
Variable controls where to save the `wpa_supplicant_conf` file to.
"""
WPA_SUPPLICANT_CONF = os.getenv("WPA_SUPPLICANT_CONF")
SUDO_MODE = os.getenv("SUDO_MODE")


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
