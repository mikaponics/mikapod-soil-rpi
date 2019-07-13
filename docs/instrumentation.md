#TODO: IMPLEMENT

# Mikaponics IoT - Mikapod (Soil) - Instrument
The ``instrument_service.py`` application is responsible for providing service for polling the instrumentation in the Arduino sensor's and sends the data to the storage application through ``rpc``.

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
    pip install python-dotenv                 # Environment variable loader.
    pip install Pyro4                         # Distrubted objects library.
    pip install pyserial                      # Serial USB Communication library for Python.
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
  python storage_service.py
  ```

3. Verify our service is working:

  ```
  pyro4-nsc list
  ```

## Automatic Startup on Boot
This micro-service is found in the ``mikapod/instrumentation_service.py`` file and is responsible for handling the attached instrumentats (humidity, termperature, light, etc) and providing an interface for accessing any of the data within any of the operating instrumentations.

1. While being logged in as ``pi`` run the following:

    ```
    $ sudo vi /etc/systemd/system/mikapod_instrumentation.service
    ```

2. Copy and paste the following contents.

    ```
    [Unit]
    Description=Mikapod Instrumentation Interface Daemon
    After=multi-user.target

    [Service]
    Type=idle
    ExecStart=/home/pi/mikapod-py/env/bin/python3.5 /home/pi/mikapod-py/mikapod/instrumentation_service.py
    Restart=on-failure
    KillSignal=SIGTERM

    [Install]
    WantedBy=multi-user.target
    ```

3. We can now start the Gunicorn service we created and enable it so that it starts at boot:

    ```
    sudo systemctl start mikapod_instrumentation
    sudo systemctl enable mikapod_instrumentation
    ```

4. Confirm our service is running.

    ```
    sudo systemctl status mikapod_instrumentation.service
    ```

5. If the service is working correctly you should see something like this at the bottom:

    ```
    raspberrypi systemd[1]: Started Mikapod Instrumentation Interface Daemon.
    ```

6. Congradulations, you have setup instrumentation micro-service! All other micro-services can now poll the latest data from the instruments we have attached.

7. If you see any problems, run the following service to see what is wrong. More information can be found in [this article](https://unix.stackexchange.com/a/225407).

    ```
    sudo journalctl -u mikapod_instrumentation
    ```
