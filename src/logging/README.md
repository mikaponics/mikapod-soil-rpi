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
    pip install python-dotenv                 # Environment variable loader
    pip install Pyro4                         # Distrubted objects library
    ```

4. In this directorym create a file called ``.env`` and populate it with the following content:

    ```
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
    ```

5. Please change the contents of the ``.env`` file to match the configuration found in your systen.

## Usage


1. Turn on our distrubted objects name-server if it has not been done already. If you are about to run this command, do not close the terminal.

  ```
  python -m Pyro4.naming
  ```

2. Open up another terminal and run our service, make sure we have the above code running before running the code below.

  ```
  python logging_service.py
  ```

3. (OPTIONAL) You can try out the fake data logger too.

  ```
  python fake_logging_service.py
  ```

4. Verify our service is working:

  ```
  pyro4-nsc list
  ```
