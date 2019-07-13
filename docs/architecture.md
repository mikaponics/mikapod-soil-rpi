# Purpose

The purpose of this project is to provide a simple device which users can configure to connect to the internet and begin upload time-series data for the plant(s) they are monitoring.

# How does the device work?

1. User registers the sensors / instruments the device will be using through the [Mikaponics website](https://github.com/mikaponics/mikaponics-front) or Mikaponics staff will manually registering through the [Mikaponics API web-service](https://github.com/mikaponics/mikaponics-back). Once registered, the API web-service will provide ``UUID`` values for each sensor / instrument.

2. User registers ``OAuth 2.0 Client Credentials`` from the [Mikaponics API web-service](https://github.com/mikaponics/mikaponics-back) either manually or done by staff to be provided with the ``client_id`` and ``client_secret`` values.

3. This device pulls the [Mikaponics Soil (Arduino) device](https://github.com/mikaponics/mikapod-soil-arduino) every minute to get the latest sensor data.

4. This device saves the time-series data to the local database.

5. This device uploads the time-series data to [Mikaponics API web-service](https://github.com/mikaponics/mikaponics-back) it has saved in the local database. This process uses the registered UUID and OAuth credentials.

6. Local time series data gets purged once successfully uploaded.

# How is the software work?

1. The application is structured in a **microservices architecture** . This means every application is an independent program, running indepdently in the system.

2. Every application is connected to each other using the ``Python`` remote distrubuted objects library called [``Pyro4``](https://github.com/irmen/Pyro4).

3. Every independent program is called a ``service`` in our system.

4. Every ``service`` automatically boots at startup

# What Raspberry Pi devices does this code work on?

The following devices were tested and confirmed working:

* Raspberry Pi 3 Model A+ 1.4GHz
