# Developer

1. (Optional) Turn on our distrubted objects name-server if it has not been done already. If you are about to run this command, do not close the terminal.

        $ python -m Pyro4.naming

2. Open up another terminal and run our service, make sure we have the above code running before running the code below.

        $ python storage_service.py

3. Open up another terminal and run the colling command to verify our service is working:

        $ pyro4-nsc list

# Production

1. While being logged in as ``pi`` run the following:

        $ sudo vi /etc/systemd/system/mikapod_storage.service

2. Copy and paste the following contents.

        [Unit]
        Description=Mikapod Storage Daemon
        After=multi-user.target

        [Service]
        Type=idle
        ExecStart=/home/pi/mikapod-soil-rpi/scripts/storage.sh
        Restart=on-failure
        KillSignal=SIGTERM

        [Install]
        WantedBy=multi-user.target


3. We can now start the Gunicorn service we created and enable it so that it starts at boot:

        sudo systemctl start mikapod_storage
        sudo systemctl enable mikapod_storage

4. Confirm our service is running.

        sudo systemctl status mikapod_storage.service

5. If the service is working correctly you should see something like this at the bottom:

        raspberrypi systemd[1]: Started Mikapod Storage Daemon.

6. Congradulations, you have setup storage micro-service! All other micro-services this application uses will powered by the data stored.

7. If you see any problems, run the following service to see what is wrong. More information can be found in [this article](https://unix.stackexchange.com/a/225407).

        sudo journalctl -u mikapod_storage
