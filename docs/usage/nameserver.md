# Developer
Run the following command and keep the console window open.

        $(env) python -m Pyro4.naming


# Production
The following set of instructions will show how to have **RPC Nameserver** application to automatically startup when the system boots using ``systemd``.

1. While being logged in as ``pi`` run the following:

        $ sudo vi /etc/systemd/system/mikapod_nameserver.service

2. Copy and paste the following contents.

        [Unit]
        Description=Mikapod Nameserver Daemon
        After=multi-user.target

        [Service]
        Type=idle
        User=pi
        ExecStart=/home/pi/mikapod-soil-rpi/scripts/nameserver.sh
        Restart=on-failure
        KillSignal=SIGTERM

        [Install]
        WantedBy=multi-user.target

3. We can now start the Gunicorn service we created and enable it so that it starts at boot:

        sudo systemctl start mikapod_nameserver
        sudo systemctl enable mikapod_nameserver

4. Confirm our service is running.

        systemctl status mikapod_nameserver.service

5. If the service is working correctly you should not see any errors. Congradulations, you have setup the name server which will tie in all the micro-services. In the next few sections we will see how to setup those individual micro-services.
