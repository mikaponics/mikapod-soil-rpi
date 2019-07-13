#TODO: IMPLEMENT

# Mikaponics IoT - Remote Service
The ``remote_service.py`` application is responsible for interfacing with [Mikaponics Backend Web-Service](https://github.com/mikaponics/mikaponics-back).

## Installation

1. Setup our virtual environment

    ```bash
    virtualenv -p python3.6 env
    ```

2. Now lets activate virtual environment

    ```bash
    source env/bin/activate
    ```

3. Install the ``Python`` dependencies.

    ```bash
    pip install pytz                          # World Timezone Definitions
    pip install Pyro4                         # Distrubted objects library.
    pip install python-dotenv                 # Environment variable loader.
    pip install requests                      # HTTP Requests handler library.
    pip install requests_oauthlib             # oAuth 2.0 Support with Requests library.
    pip install msgpack-python                # Message Pack Serializer Library.
    ```

4. In this directorym create a file called ``.env`` and populate it with the following content:

    ```
    DATABASE=storage.db
    LOCAL_TIMEZONE_NAME=America/Toronto
    ```

5. Please change the contents of the ``.env`` file to match the configuration found in your systen.

## Usage


1. Turn on our distrubted objects name-server if it has not been done already. If you are about to run this command, do not close the terminal.

  ```
  python -m Pyro4.naming
  ```

2. Open up another terminal and run our service, make sure we have the above code running before running the code below.

  ```
  python remote_service.py
  ```

3. Verify our service is working:

  ```
  pyro4-nsc list
  ```


## Remote Service
This micro-service is found in the ``mikapod/remote_service.py`` file and is responsible for polling the latest instrumentation data and saving it to our local persistent storage.

1. While being logged in as ``pi`` run the following:

    ```
    $ sudo vi /etc/systemd/system/mikapod_remote.service
    ```

2. Copy and paste the following contents.

    ```
    [Unit]
    Description=Mikapod Remote Daemon
    After=multi-user.target

    [Service]
    Type=idle
    ExecStart=/home/pi/mikapod-py/env/bin/python3.5 /home/pi/mikapod-py/mikapod/remote_service.py
    Restart=on-failure
    KillSignal=SIGTERM

    [Install]
    WantedBy=multi-user.target
    ```

3. We can now start the Gunicorn service we created and enable it so that it starts at boot:

    ```
    sudo systemctl start mikapod_remote
    sudo systemctl enable mikapod_remote
    ```

4. Confirm our service is running.

    ```
    sudo systemctl status mikapod_remote.service
    ```

5. If the service is working correctly you should see something like this at the bottom:

    ```
    raspberrypi systemd[1]: Started Mikapod Data Logging Daemon.
    ```

6. Congradulations, you have setup the remote micro-service! This service will be polling the latest local persistent storage data and submit it to the remote API web-service.

7. If you see any problems, run the following service to see what is wrong. More information can be found in [this article](https://unix.stackexchange.com/a/225407).

    ```
    sudo journalctl -u mikapod_remote
    ```
