#!/usr/bin/python
# -*- coding: utf-8 -*-
import datetime
import signal
import time
import os
import subprocess
import sys

from foundation import *


"""
EXAMPLE:
python wifi_config_cmd CA "wifi ssid" "wifi password"
"""


class ServiceExit(Exception):
    """
    Custom exception which is used to trigger the clean exit
    of all running threads and the main program.
    """
    pass


def onServiceShutdownHandler(signum, frame):
    """
    Function to be called by our `SIGINT` and `SIGTERM` handlers.
    """
    print("-------------------------------------------------------------------")
    print(getDT(), '| WIFI CONFIG | Caught signal %d' % signum)
    print("-------------------------------------------------------------------")
    raise ServiceExit


class WifiConfigCommand(object):

    def __init__(self):
        pass

    def update_wifi(self, country, ssid, ps):
        # write wifi config to file
        f = open('wifi.conf', 'w')
        f.write('country='+country+'\n')
        f.write('ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev\n')
        f.write('update_config=1\n')
        f.write('\n')
        f.write('network={\n')
        f.write('    ssid="' + ssid + '"\n')
        f.write('    psk="' + ps + '"\n')
        f.write('}\n')
        f.close()

        cmd = 'mv wifi.conf ' + WPA_SUPPLICANT_CONF
        cmd_result = ""
        cmd_result = os.system(cmd)
        print(getDT(), '| WIFI CONFIG | '+ cmd + " - " + str(cmd_result) )

        # restart wifi adapter
        cmd = SUDO_MODE + 'ifdown wlan0'
        cmd_result = os.system(cmd)
        print(getDT(), '| WIFI CONFIG | '+ cmd + " - " + str(cmd_result) )

        time.sleep(2) # Give time for the wifi card to go down.

        cmd = SUDO_MODE + 'ifup wlan0'
        cmd_result = os.system(cmd)
        print(getDT(), '| WIFI CONFIG | '+ cmd + " - " + str(cmd_result) )

        time.sleep(10) # Give time for the wifi card to go up.

        cmd = 'iwconfig wlan0'
        cmd_result = os.system(cmd)
        print(getDT(), '| WIFI CONFIG | '+ cmd + " - " + str(cmd_result) )

        cmd = 'ifconfig wlan0'
        cmd_result = os.system(cmd)
        print(getDT(), '| WIFI CONFIG | '+ " - " + str(cmd_result) )

        p = subprocess.Popen(['ifconfig', 'wlan0'], stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)

        out, err = p.communicate()
        print(getDT(), '| WIFI CONFIG | OUT: ' + str(out))
        print(getDT(), '| WIFI CONFIG | ERR: ' + str(err))
        return True

    def runOnMainLoop(self, args):
        """
        Function is the main loop of the application.
        """
        print(getDT(), "| WIFI CONFIG | Register the signal handlers.")
        signal.signal(signal.SIGTERM, onServiceShutdownHandler)
        signal.signal(signal.SIGINT, onServiceShutdownHandler)

        print(getDT(), "| WIFI CONFIG | Starting main program.")

        try:
            country = args[1]
            ssid = args[2]
            ps = args[3]
            return self.update_wifi(country, ssid, ps)
        except ServiceExit:
            print(getDT(), "| WIFI CONFIG | Gracefully shutting down.")
        print(getDT(), "| WIFI CONFIG | Exiting main program.")

if __name__ == "__main__":
    """
    Main entry into the main program.
    """
    app = WifiConfigCommand()
    app.runOnMainLoop(sys.argv)
