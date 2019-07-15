# Usage
1. Turn on our distrubted objects name-server if it has not been done already. If you are about to run this command, do not close the terminal.

        $ python -m Pyro4.naming

2. Open up another terminal and run our service, make sure we have the above code running before running the code below.

        $ python remote_service.py

3. Open up another terminal and run the colling command to verify our service is working:

        $ pyro4-nsc list


## Remote Service
This micro-service is found in the ``mikapod/remote_service.py`` file and is responsible for polling the latest instrumentation data and saving it to our local persistent storage.

1. While being logged in as ``pi`` run the following:

        $ sudo vi /etc/systemd/system/mikapod_remote.service

2. Copy and paste the following contents.

        [Unit]
        Description=Mikapod Remote Daemon
        After=multi-user.target

        [Service]
        Type=idle
        ExecStart=/home/pi/mikapod-soil-rpi/scripts/remote.sh
        Restart=on-failure
        KillSignal=SIGTERM

        [Install]
        WantedBy=multi-user.target

3. We can now start the Gunicorn service we created and enable it so that it starts at boot:

        sudo systemctl start mikapod_remote
        sudo systemctl enable mikapod_remote

4. Confirm our service is running.

        sudo systemctl status mikapod_remote.service

5. If the service is working correctly you should see something like this at the bottom:

        raspberrypi systemd[1]: Started Mikapod Remote Daemon.

6. Congradulations, you have setup the remote micro-service! This service will be polling the latest local persistent storage data and submit it to the remote API web-service.

7. If you see any problems, run the following service to see what is wrong. More information can be found in [this article](https://unix.stackexchange.com/a/225407).

        sudo journalctl -u mikapod_remote
