#!/usr/bin/python
# -*- coding: utf-8 -*-
import datetime
import signal
import time
import json

from serial import Serial
import Pyro4
import pytz

from foundation import *


"""
THE PURPOSE OF THIS CODE IS TO PROVIDE A STREAM OF DATA FROM THE SERIAL TERMINALS
TO THE PROGRAMMERS CONSOLE TO SEE WHAT THE ARDUINO DEVICE IS RETURNING. THIS
CODE IS TO BE USED FOR TESTING PURPOSES ONLY! **DO NOT USE IN PRODUCTION**
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
    print(getDT(), '| SERIAL TERMINAL STREAM | Caught signal %d' % signum)
    print("-------------------------------------------------------------------")
    raise ServiceExit


class SerialTerminalPrint(object):
    """
    Service interacts with the external device (Arduino) and prints the data
    on a specific interval to the user's console.
    """

    def __init__(self):
        '''
        Wait until our computer can connect to the external device (Ardunio)
        over serial USB communication to begin running our program.
        '''
        try:
            self.__serial = Serial(SERIAL_PORT, SERIAL_BAUD, timeout=SERIAL_TIMEOUT)
            time.sleep(2) # Wait for serial terminal to setup.
            print(getDT(), "| SERIAL TERMINAL STREAM | Successfully connected to serial port:", SERIAL_PORT);
        except Exception as e:
            if "could not open port" in str(e):
                print(getDT(), "| SERIAL TERMINAL STREAM | Could not connect to serial port:", SERIAL_PORT);
                exit()

        '''
        Load up our application variables.
        '''
        self.__storage = Pyro4.Proxy("PYRONAME:mikapod.storage")

    def runOnMainLoop(self):
        """
        Function is the main loop of the application.
        """
        print(getDT(), "| SERIAL TERMINAL STREAM | Register the signal handlers.")
        signal.signal(signal.SIGTERM, onServiceShutdownHandler)
        signal.signal(signal.SIGINT, onServiceShutdownHandler)

        print(getDT(), "| SERIAL TERMINAL STREAM | Starting main program.")
        try:
            self.runOperationLoop()
        except ServiceExit:
            print(getDT(), "| SERIAL TERMINAL STREAM | Gracefully shutting down.")
        print(getDT(), "| SERIAL TERMINAL STREAM | Exiting main program.")

    def runOperationLoop(self):
        # Keep running the main runtime loop with various
        # being inputted for a frame of reference in the computations
        # along with a few computations.
        while True:
            byte_data = self.__serial.readline()
            string_data = byte_data.decode('UTF-8') # NOTE: https://stackoverflow.com/questions/6269765/what-does-the-b-character-do-in-front-of-a-string-literal#6273618

            # Check to see if ANY data was returned from the serial port, if
            # there was then we load up the string
            if len(string_data) > 0:
                array_data = [x.strip() for x in string_data.split(',')]
                print(getDT(), "| SERIAL TERMINAL STREAM | Output - Pre:"+string_data+"\n")
                print(getDT(), "| SERIAL TERMINAL STREAM | Output - Post:"+str(array_data)+"\n")

                commandID = int(array_data[0])
                var = array_data[1]
                opcode = array_data[2]

                if int(commandID) == SET_WIFI_COMMAND_ID:
                    self.changeWiFiCommand(var, opcode)

    def changeWiFiCommand(self, ssid, pw):
        print(getDT(), "| SERIAL TERMINAL STREAM | Set Wifi w/ SSID `"+ssid+"` and PW `"+pw+"`.\n")


if __name__ == "__main__":
    """
    Main entry into the main program.
    """
    app = SerialTerminalPrint()
    app.runOnMainLoop()
