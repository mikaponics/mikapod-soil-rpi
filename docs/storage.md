# Overview
The ``storage_service.py`` application is responsible for providing an interface for all applications to access and GET/SET key-value paired data in a local database.

## Installation

1. Setup our virtual environment

        $ cd ~/mikapod-soil/src/services/storage
        $ virtualenv -p python3.6 env

2. Now lets activate virtual environment

        $ source env/bin/activate

3. Install the ``Python`` dependencies.

        $ pip install pytz                          # World Timezone Definitions
        $ pip install python-dotenv                 # Environment variable loader.
        $ pip install Pyro4                         # Distrubted objects library.
        $ pip install peewee                        # Peewee is a simple and small ORM.

4. In this directorym create a file called ``.env`` and populate it with the following content:

        DATABASE=storage.db
        LOCAL_TIMEZONE_NAME=America/Toronto

5. Please change the contents of the ``.env`` file to match the configuration found in your systen.


## Usage


1. (Optional) Turn on our distrubted objects name-server if it has not been done already. If you are about to run this command, do not close the terminal.

        python -m Pyro4.naming

2. Open up another terminal and run our service, make sure we have the above code running before running the code below.

        python storage_service.py

3. Verify our service is working:

        pyro4-nsc list

##  Automatic Startup on Boot

1. While being logged in as ``pi`` run the following:

        $ sudo vi /etc/systemd/system/mikapod_storage.service

2. Copy and paste the following contents.

        [Unit]
        Description=Mikapod Storage Daemon
        After=multi-user.target

        [Service]
        Type=idle
        ExecStart=/home/pi/mikapod-py/env/bin/python3.5 /home/pi/mikapod-py/mikapod/storage_service.py
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
