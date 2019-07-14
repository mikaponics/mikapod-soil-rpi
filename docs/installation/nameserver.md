# Instructions
Follow these instructions to begin setting up the RPC nameserver.

1. Run the following.

        $ cd ~/mikapod-soil

2. Setup our virtual environment

        $ virtualenv -p python3.6 env

3. Now lets activate virtual environment

        $ source env/bin/activate

4. Install the ``Python`` dependencies.

        $(env) pip install Pyro4                         # Distrubted objects library.

5. Run the following command and keep the console window open.

        $(env) python -m Pyro4.naming

6. If the application runs and nothing gets displayed afterwords then congradulations you have setup the service.

# Notes:
The nameserver must always run in the background, as a result:

1. If you programming on your local developer machine, you can open a new terminal window and have this application running while you code.

2. If you are running in production then you need to have this application setup in ``systemctl`` on boottime so it is always running.
