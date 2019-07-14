# Instructions
1. Setup our virtual environment

        $ cd ~/mikapod-soil-rpi/src/services/storage
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

# Environment Variables

## DATABASE
This is the name of the database, keep it simple and just name it as "storage.db".

## LOCAL_TIMEZONE_NAME
This is the timezone name used by our device. You can get a complete list of timezones by [clicking here](https://stackoverflow.com/q/13866926).
