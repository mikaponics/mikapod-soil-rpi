# Nameserver
Follow these instructions to begin setting up the RPC nameserver.

1. Run the following.

        $ cd ~/mikapod-soil-rpi

2. Setup our virtual environment

        $ virtualenv -p python3.6 env

3. Now lets activate virtual environment

        $ source env/bin/activate

4. Install the ``Python`` dependencies.

        $(env) pip install Pyro4                         # Distrubted objects library.

5. Run the following command and keep the console window open.

        $(env) python -m Pyro4.naming

6. If the application runs and nothing gets displayed afterwords then congradulations you have setup the service.

**Notes:**
The nameserver must always run in the background, as a result:

1. If you programming on your local developer machine, you can open a new terminal window and have this application running while you code.

2. If you are running in production then you need to have this application setup in ``systemctl`` on boottime so it is always running.

# Storage
1. Setup our virtual environment

        $ cd ~/mikapod-soil-rpi/src/storage/
        $ virtualenv -p python3.6 env

2. Now lets activate virtual environment

        $ source env/bin/activate

3. Install the ``Python`` dependencies.

        $(env) pip install pytz                          # World Timezone Definitions
        $(env) pip install python-dotenv                 # Environment variable loader.
        $(env) pip install Pyro4                         # Distrubted objects library.
        $(env) pip install peewee                        # Peewee is a simple and small ORM.

4. In this directorym create a file called ``.env`` and populate it with the following content:

        DATABASE=storage.db
        LOCAL_TIMEZONE_NAME=America/Toronto

5. Please change the contents of the ``.env`` file to match the configuration found in your systen.

6. When you are ready, run the service.

        $(env) python storage_service.py

# Instruments

1. Setup our virtual environment

        $ virtualenv -p python3.6 env

2. Now lets activate virtual environment

    $ source env/bin/activate

3. Install the ``Python`` dependencies.

        $(env) pip install pytz                          # World Timezone Definitions
        $(env) pip install python-dotenv                 # Environment variable loader.
        $(env) pip install Pyro4                         # Distrubted objects library.
        $(env) pip install pyserial                      # Serial USB Communication library for Python.

4. In this directorym create a file called ``.env`` and populate it with the following content:

        ## APPLICATION CONFIGURATION
        #

        SERIAL_PORT=/dev/ttyACM0
        SERIAL_BAUD=9600
        SERIAL_TIMEOUT=60
        LOCAL_TIMEZONE_NAME=America/Toronto
        TIME_STEP_IN_MINUTES=1
        TIME_STEP=00:01:00

5. Please change the contents of the ``.env`` file to match the configuration found in your systen.

# Logging
1. Setup our virtual environment

        $ virtualenv -p python3.6 env

2. Now lets activate virtual environment

        $ source env/bin/activate

3. Install the ``Python`` dependencies.

        $(env) pip install pytz                          # World Timezone Definitions
        $(env) pip install python-dotenv                 # Environment variable loader
        $(env) pip install Pyro4                         # Distrubted objects library

4. In this directorym create a file called ``.env`` and populate it with the following content:

        ## APPLICATION CONFIGURATION
        #

        LOCAL_TIMEZONE_NAME=America/Toronto
        TIME_STEP_IN_MINUTES=1
        TIME_STEP=00:01:00


        ## API WEB-SERVICE CONFIGURATION
        #

        HUMIDITY_INSTRUMENT_UUID=02a1ec41-1192-4ac8-a5b0-0568c7a6cea9
        TEMPERATURE_INSTRUMENT_UUID=a305253f-4314-479f-971e-ed3cdcf9d238
        ILLUMINANCE_INSTRUMENT_UUID=ce04530b-3e7c-45d4-9d15-f865fc22beea
        PRESSURE_INSTRUMENT_UUID=45c628d0-adf5-460e-9fb3-c45b641cfd92
        POWER_USAGE_UUID=533d2f33-a1e8-4cde-bc4e-41ff0ebfb016
        ALTITUDE_INSTRUMENT_UUID=b1a763af-b831-4188-8e39-0bf131891d79
        SOIL_MOISTURE_INSTRUMENT_UUID=b1a763af-b831-4188-8e39-0bf131891d79


5. Please change the contents of the ``.env`` file to match the configuration found in your systen.

# Remote

1. Setup our virtual environment

        $ virtualenv -p python3.6 env

2. Now lets activate virtual environment

        $ source env/bin/activate

3. Install the ``Python`` dependencies.

        $(env) pip install pytz                          # World Timezone Definitions
        $(env) pip install Pyro4                         # Distrubted objects library.
        $(env) pip install python-dotenv                 # Environment variable loader.
        $(env) pip install requests                      # HTTP Requests handler library.
        $(env) pip install requests_oauthlib             # oAuth 2.0 Support with Requests library.
        $(env) pip install msgpack-python                # Message Pack Serializer Library.

4. In this directorym create a file called ``.env`` and populate it with the following content:

        ## API WEB-SERVICE CONFIGURATION
        #

        WEB_SERVICE_URL=http://localhost:8000
        WEB_SERVICE_CLIENT_ID=0wndkLXCfUxpeYrVP34tWABLowq85VM7DL5PezJ4
        WEB_SERVICE_CLIENT_SECRET=lDuERWYNgRZ5sMQDkYkxFGrTTC5Nvam5Q1jJDfzWvqxiVQ3c81Z3KCYhPjqajWHPEuaQBPvUBrjsxXjnUtiaN8QYyQzhkbcKjJDXi9S7dSlMK8apOSTTJXr0cxF1acAC
        WEB_SERVICE_DEVICE_UUID=fe054342-b099-4d4c-aad4-411231af5ce3


        ## APPLICATION CONFIGURATION
        #

        LOCAL_TIMEZONE_NAME=America/Toronto


5. Please change the contents of the ``.env`` file to match the configuration found in your systen.
