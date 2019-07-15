# Developer

1. Turn on our distrubted objects name-server if it has not been done already. If you are about to run this command, do not close the terminal.

        $ python -m Pyro4.naming

2. Open up another terminal and run our service, make sure we have the above code running before running the code below.

        $ python storage_service.py

3. Open up another terminal and run the colling command to verify our service is working:

        $ pyro4-nsc list

# Production
This micro-service is found in the ``mikapod/instrumentation_service.py`` file and is responsible for handling the attached instrumentats (humidity, termperature, light, etc) and providing an interface for accessing any of the data within any of the operating instrumentations.

1. While being logged in as ``pi`` run the following:

        $ sudo vi /etc/systemd/system/mikapod_instruments.service

2. Copy and paste the following contents.

        [Unit]
        Description=Mikapod Instruments Interface Daemon
        After=multi-user.target

        [Service]
        Type=idle
        ExecStart=/home/pi/mikapod-soil-rpi/env/bin/python3.5 /home/pi/mikapod-soil-rpi/src/instrument/instrument_service.py
        Restart=on-failure
        KillSignal=SIGTERM

        [Install]
        WantedBy=multi-user.target

3. We can now start the Gunicorn service we created and enable it so that it starts at boot:

        $ sudo systemctl start mikapod_instruments
        $ sudo systemctl enable mikapod_instruments

4. Confirm our service is running.

        $ sudo systemctl status mikapod_instruments.service

5. If the service is working correctly you should see something like this at the bottom:

        raspberrypi systemd[1]: Started Mikapod Instrumentation Interface Daemon.

6. Congradulations, you have setup instrumentation micro-service! All other micro-services can now poll the latest data from the instruments we have attached.

7. If you see any problems, run the following service to see what is wrong. More information can be found in [this article](https://unix.stackexchange.com/a/225407).

        $ sudo journalctl -u mikapod_instruments
