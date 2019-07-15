#!/bin/bash
# Script will load up the ``Pyro4`` name server to register our distributed objects.
# This script will be run by our ``systemctl``service.
source /home/pi/mikapod-soil-rpi/env/bin/activate
pyro4-ns
