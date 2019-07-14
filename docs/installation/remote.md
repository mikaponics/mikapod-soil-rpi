# Instructions

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

        LOCAL_TIMEZONE_NAME=America/Toronto

5. Please change the contents of the ``.env`` file to match the configuration found in your systen.

# Environment Variables

## LOCAL_TIMEZONE_NAME
This is the timezone name used by our device. You can get a complete list of timezones by [clicking here](https://stackoverflow.com/q/13866926).
